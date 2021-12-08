from collections import defaultdict
from json import load
from gen_items import gen_bases


def main():
	# generate all possible ngrams
	ngrams = defaultdict(set)
	bad_ngrams = set()
	with open('sc_unique.json') as f:
		sc_bases = load(f)
	with open('hc_unique.json') as f:
		hc_bases = load(f)
	good_bases = {x for x in sc_bases | hc_bases}
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
		seen_combo = set()
		# only need to keep track of 1 unique key per base
		for key in sorted(ngrams[base], key=len):
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