from collections import defaultdict

from gen_item_lists import bases


# TODO: Handle implicits
def main():
	ngrams = defaultdict(set)
	for typ in bases:
		for tags in bases[typ]:
			for item in bases[typ][tags]:
				base = item['name'].lower()
				for i in range(len(base)):
					for j in range(i+1, len(base) + 1):
						ch = base[i:j]
						if ch[0] != ' ' and ch[-1] != ' ':
							ngrams[base].add(ch)

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