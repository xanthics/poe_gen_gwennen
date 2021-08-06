from collections import defaultdict

from gen_items import gen_bases


def main():
	ngrams = defaultdict(set)
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
			f.write(f'\t"{base}": {child[base]},\n')
		f.write('}\n\n')

		f.write('ngrams = {\n')
		for base in sorted(ngrams):
			f.write(f'\t"{base}": {ngrams[base]},\n')
		f.write('}')


if __name__ == '__main__':
	main()