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
	max_ngram_len = 8  # all good bases can generate a unique ngram within 8 characters
	for item in gen_bases:
		if item['name'] in good_bases:
			continue
		base = item['name'].lower()
		for i in range(len(base)):
			for j in range(i+1, len(base) + 1):
				ch = base[i:j]
				if len(ch) > max_ngram_len:
					continue
				if ch[0] != ' ' and ch[-1] != ' ':
					bad_ngrams.add(ch.lower())
		if 'implicit' in item:
			for x in item['implicit']:
				for i in range(len(x)):
					for j in range(i + 1, len(x) + 1):
						ch = x[i:j]
						if len(ch) > max_ngram_len:
							continue
						bad_ngrams.add(ch.lower())
	for item in gen_bases:
		if item['name'] not in good_bases:
			continue
		base = item['name'].lower()
		for i in range(len(base)):
			for j in range(i+1, len(base) + 1):
				ch = base[i:j]
				if len(ch) > max_ngram_len:
					continue
				if ch[0] != ' ' and ch[-1] != ' ':
					ngrams[base].add(ch.lower())
		if 'implicit' in item:
			for x in item['implicit']:
				for i in range(len(x)):
					for j in range(i + 1, len(x) + 1):
						ch = x[i:j]
						if len(ch) > max_ngram_len:
							continue
						ngrams[base].add(ch.lower())
		ngrams[base] -= bad_ngrams
	# remove all ngrams that are too common
	threshold = 3
	counts = defaultdict(int)
	for base in ngrams:
		for gram in ngrams[base]:
			counts[gram] += 1
	common_grams = set()
	for item in counts:
		if counts[item] > threshold:
			common_grams.add(item)
	for base in ngrams.copy():
		ngrams[base] -= common_grams
		if not ngrams[base]:
			print(f"removing {base} because it is empty")
			del ngrams[base]
	ngrams['tricorne'] = {'tricorne'}
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