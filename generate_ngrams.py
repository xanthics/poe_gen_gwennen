from collections import defaultdict

from gen_items import gen_bases


def main():
	# generate all possible ngrams
	ngrams = defaultdict(set)
	# seed gen_bases with bad words to match on
	gen_bases.extend([
		{'name': 'Implicit Modifier'},
		{'name': 'Evasion Rating'},
		{'name': "Energy Shield"},
		{'name': "Armour"},
		{'name': 'Physical Damage'},
		{'name': 'Critical Strike Chance'},
		{'name': 'Attacks per Second'},
		{'name': 'Weapon Range'},
		{'name': 'Item Level'},
		{'name': 'Requires'},
		{'name': 'Str'},
		{'name': 'Dex'},
		{'name': 'Int'}
	])
	for item in gen_bases:
		base = item['name'].lower()
		for i in range(len(base)):
			for j in range(i+1, len(base) + 1):
				ch = base[i:j]
				if len(ch) > 46:
					continue
				if ch[0] != ' ' and ch[-1] != ' ':
					ngrams[base].add(ch.lower())
		if 'implicit' in item:
			for x in item['implicit']:
				for i in range(len(x)):
					for j in range(i + 1, len(x) + 1):
						ch = x[i:j]
						if len(ch) > 46:
							continue
						if ch[0] != ' ' and ch[-1] != ' ':
							ngrams[base].add(ch.lower())
	# remove all ngrams that are too common
	threshold = 5
	counts = defaultdict(int)
	for base in ngrams:
		for gram in ngrams[base]:
			counts[gram] += 1
	common_grams = set()
	for item in counts:
		if counts[item] >= threshold:
			common_grams.add(item)
	for base in ngrams.copy():
		ngrams[base] -= common_grams
		if not ngrams[base]:
			print(f"removing {base} because it is empty")
			del ngrams[base]
	ngrams['sai'] = {'sai'}
	# find all bases that are a substring of other base(s)
	searchpool = sorted(ngrams, key=len)
	child = {}
	for c, base in enumerate(searchpool):
		if any(base in x for x in searchpool[c+1:]):
			child[base] = [x for x in searchpool[c+1:] if base in x]
	for c in child:
		for bigger_base in child[c]:
			ngrams[f"{bigger_base}§{c}"] = ngrams[bigger_base] - ngrams[c]

	with open('ngram_generated.py', 'w', encoding='utf-8') as f:
		f.write('subnames = {\n')
		for base in child:
			f.write(f'\t"{base}": {sorted(child[base])},\n')
		f.write('}\n\n')

		f.write('ngrams = {\n')
		for base in sorted(ngrams):
			# to keep the order stable for spotting differences
			n_sort = '", "'.join(sorted(ngrams[base]))
			f.write(f'\t"{base}": {{"{n_sort}"}},\n')
		f.write('}')


if __name__ == '__main__':
	main()