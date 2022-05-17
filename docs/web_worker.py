from browser import bind, self
from ngram_generated import ngrams, subnames


@bind(self, "message")
def message(evt):
	if evt.data[0] == 'init':
		good_bases = set(evt.data[1])
		overlap_bases = []
		for base in good_bases:
			if base in subnames:
				t_str = ' and '.join(subnames[base])
				self.send(('overlap', base, t_str))
				overlap_bases.extend(subnames[base])
		self.send(('update', "Calculating Bases and bad ngrams"))
		bad_bases = set(ngrams.keys()) - good_bases
		for base in bad_bases.copy():
			if base in overlap_bases or '§' in base and base.split('§')[1] not in overlap_bases:
				bad_bases.discard(base)
		bad_ngrams = set()
		bad_ngrams.update(*[ngrams[base] for base in bad_bases])
		good_ngrams = {}
		self.send(('update', "Updating selected bases available ngrams"))
		for base in good_bases:
			good_ngrams[base] = ngrams[base] - bad_ngrams

		self.send(('update', "Finding best choices"))
		greedy_choice = {}
		while good_ngrams:
			table = {}
			for base in good_ngrams:
				if not good_ngrams[base]:
					self.send(('debug', f"{base} has no suitable substring"))
					good_ngrams.pop(base)
					continue
				for ng in good_ngrams[base]:
					if ng not in table:
						table[ng] = []
					table[ng].append(base)
			ranking = []
			for ng in table:
				ranking.append([len(ng)/len(table[ng]), ng, table[ng]])
			ranking = sorted(ranking, key=lambda x: x[0])
			mychoice = ranking[0]
			greedy_choice[mychoice[1]] = mychoice[2]
			for base in mychoice[2]:
				good_ngrams.pop(base)
		self.send(('update', "Building knapsacked strings"))
		builder = sorted(greedy_choice, key=len, reverse=True)
		for ng in builder[:-1]:
			self.send(('debug', f"{repr(ng)}: '{greedy_choice[ng]}'"))
		if len(builder) > 1:
			self.send(('debug', f"{repr(builder[-1])}: '{greedy_choice[builder[-1]]}'"))

		k_bag_str = []
		while builder:
			current_k_str = f'"{builder[0]}'
			builder.pop(0)
			for s in builder[:]:
				if len(current_k_str) + len(s) < 49:
					current_k_str += '|' + s
					builder.remove(s)
			k_bag_str.append(current_k_str + '"')
		self.send(('done', k_bag_str))

