from collections import defaultdict
from gen_items import gen_bases


def gen_grams(unique_data):
	# generate all possible ngrams
	ngrams = defaultdict(set)
	bad_ngrams = set()
	good_bases = {x for x in unique_data['sc'] | unique_data['hc']}
	# seed gen_bases with bad words to match on
	gen_bases.extend([
		{'name': x} for x in {'Implicit Modifier', 'Evasion Rating', "Energy Shield", "Armour", 'Physical Damage', 'Critical Strike Chance',
		                      'Attacks per Second', 'Weapon Range', 'Item Level', 'Requires', 'Str', 'Dex', 'Int'}
	])
	# Todo: add proper support for items with base types that have multiple implicits.  EG two-stone and Call of the Brotherhood
	for item in gen_bases:
		base = item['name'].lower()
		if item['name'] in good_bases:
			key = ngrams[base]
		else:
			key = bad_ngrams
		for i in range(len(base)):
			for j in range(i + 1, len(base) + 1):
				ch = base[i:j]
				if ch[0] != ' ' and ch[-1] != ' ':
					key.add(ch.lower())
		if 'implicit' in item:
			for x in item['implicit']:
				for i in range(len(x)):
					for j in range(i + 1, len(x) + 1):
						ch = x[i:j]
						if ch[0] != ' ' and ch[-1] != ' ':
							bad_ngrams.add(ch.lower())
	# keep the shortest gram for pairs that have multiple matches
	counts = defaultdict(int)
	base_pairs = defaultdict(str)
	for base in ngrams:
		# first remove all bad ngrams
		ngrams[base] -= bad_ngrams
		for gram in ngrams[base]:
			counts[gram] += 1
			base_pairs[gram] += base
	for base in ngrams.copy():
		# only need to keep track of 1 unique key per base
		# double sorted for stable results
		seen_combo = set()
		for key in sorted(sorted(ngrams[base]), key=len):
			if base_pairs[key] in seen_combo:
				ngrams[base].discard(key)
			else:
				seen_combo.add(base_pairs[key])
		if not ngrams[base]:
			print(f"removing {base} because it is empty")
			del ngrams[base]
	# because noble tricorne does not have a chanceable unique (yet)
	ngrams['tricorne'] = {'tric'}
	# find all bases that are a substring of other base(s)
	searchpool = sorted(ngrams, key=len)
	child = {}
	for c, base in enumerate(searchpool):
		if any(base in x for x in searchpool[c+1:]):
			child[base] = [x for x in searchpool[c+1:] if base in x]
	for c in child:
		for bigger_base in child[c]:
			ngrams[f"{bigger_base}§{c}"] = ngrams[bigger_base] - ngrams[c]

	with open('docs/ngram_generated.py', 'w', encoding='utf-8') as f:
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
