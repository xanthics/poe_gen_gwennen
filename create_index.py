import subprocess
import os

from ninja_data import scrape_ninja
from generate_ngrams import gen_grams
from render_guide import render_guide


def update_brython():
	proc = subprocess.Popen(['brython-cli', 'install'], cwd='docs/js')
	proc.wait()
	for file in ['demo.html', 'index.html', 'README.txt', 'unicode.txt']:
		f_file = f"docs/js/{file}"
		if os.path.exists(f_file):
			os.remove(f_file)
	proc = subprocess.Popen(['brython-cli', 'make_modules'], cwd='docs')
	proc.wait()
	f_file = "docs/js/brython_stdlib.js"
	if os.path.exists(f_file):
		os.remove(f_file)


def main():
	show_10, unique_data = scrape_ninja()
	gen_grams(unique_data)
	render_guide(show_10, unique_data)

	# generate compact brython.js
	# update_brython()


if __name__ == '__main__':
	main()
