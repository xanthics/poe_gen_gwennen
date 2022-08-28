import subprocess
import os

from ninja_data import scrape_ninja
from generate_ngrams import gen_grams
from render_guide import render_guide


def safe_delete(file):
	if os.path.exists(file):
		os.remove(file)


def update_brython():
	# always run brython update when started
	safe_delete("docs/js/brython.js")
	# start installing brython js
	proc = subprocess.Popen(['brython-cli', 'install'], cwd='docs/js')
	proc.wait()
	# remove demo files that will interfere with make_modules
	for file in ['demo.html', 'index.html', 'README.txt', 'unicode.txt', 'brython_modules.js']:
		safe_delete(f"docs/js/{file}")
	# make a brython_modules.js specific to our setup
	proc = subprocess.Popen(['brython-cli', 'make_modules'], cwd='docs')
	proc.wait()
	# remove stdlib since we no longer need it
	safe_delete("docs/js/brython_stdlib.js")


def main():
	show_10, unique_data, missing_data = scrape_ninja()
	gen_grams(unique_data)
	render_guide(show_10, unique_data, missing_data)

	# generate compact brython.js
	update_brython()


if __name__ == '__main__':
	main()
