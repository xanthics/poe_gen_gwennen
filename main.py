from browser import document as doc
from browser import bind
from ngram_generated import ngrams, subnames
from browser.html import P, BR


# Function for saving changes
@bind('.save', 'change')
def save_state(ev):
	if ev.target.id == 'chaos_filter':
		c = True if doc['hide_low_value'].value == 'hide' else False
		for el in doc.get(selector="[data-value]"):
			if int(el.attrs['data-value']) >= int(ev.target.value):
				if 'container' in el.class_name:
					el.attrs['class'] = "container"
				elif 'hidden' in el.attrs:
					del el.attrs['hidden']
			else:
				if 'container' in el.class_name:
					if c:
						el.attrs['class'] = "container hidden_class"
				else:
					el.attrs['hidden'] = ''
	elif ev.target.id == 'hide_low_value':
		c = True if doc['hide_low_value'].value == 'hide' else False
		value = int(doc['chaos_filter'].value)
		for el in doc.get(selector="div[data-value]"):
			if c:
				if int(el.attrs['data-value']) >= value:
					if 'container' in el.class_name:
						el.attrs['class'] = "container"
				else:
					el.attrs['class'] = "container hidden_class"
			else:
				el.attrs['class'] = "container"


def generate_string(ev):
	doc['generated_strings'].text = ''
	good_bases = set()
	for el in doc.get(selector="input[type=checkbox]"):
		if el.checked:
			good_bases.add(el.attrs['data-id'])
	if good_bases:
		overlap_bases = []
		for base in good_bases:
			if base in subnames:
				overlap_bases.extend(subnames[base])
		bad_bases = set(ngrams.keys()) - good_bases
		bad_ngrams = set()
		for base in bad_bases:
			if base in overlap_bases or '§' in base and base.split('§')[1] not in overlap_bases:
				continue
			bad_ngrams.update(ngrams[base])
		good_ngrams = {}
		for base in good_bases:
			good_ngrams[base] = ngrams[base] - bad_ngrams

		greedy_choice = {}
		while good_ngrams:
			table = {}
			for base in good_ngrams:
				if not good_ngrams[base]:
					doc['generated_strings'] <= P(f"{base} has no suitable substring")
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
		#  Max length example " jew|rq|hon|d d|ecy| e le|r be|ge a|lk g|lth b|e"
		# max len = 48
		builder = sorted(greedy_choice, key=len, reverse=True)
		info_str = P()
		for ng in builder[:-1]:
			info_str <= f"{repr(ng)}: '{greedy_choice[ng]}'" + BR()
		if len(builder) > 1:
			info_str <= f"{repr(builder[-1])}: '{greedy_choice[builder[-1]]}'"
		k_bag_str = []
		while builder:
			current_k_str = f'"{builder[0]}'
			builder.pop(0)
			for s in builder[:]:
				if len(current_k_str) + len(s) < 49:
					current_k_str += '|' + s
					builder.remove(s)
			k_bag_str.append(current_k_str + '"')

		if k_bag_str:
			doc['generated_strings'] <= (P(f'{c}: {x}') for c, x in enumerate(k_bag_str))
			doc['generated_strings'] <= info_str
	else:
		doc['generated_strings'] <= P("No bases were selected, so no result to return.")


def select_visible(ev):
	good_bases = set()
	for el in doc.get(selector="tr[data-id]"):
		check_id = f'check-{el.attrs["data-id"].replace(" ", "_")}'
		if 'hidden' in el.attrs:
			doc[check_id].checked = False
		else:
			doc[check_id].checked = True


doc["generate"].bind("click", generate_string)
doc["select_visible"].bind("click", select_visible)
del doc['loading']