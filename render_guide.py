from jinja2 import Environment, FileSystemLoader
from htmlmin import minify
from datetime import datetime
from collections import defaultdict


def simple_format(value):
	"""Simple template example for formatting a number"""
	if value > 1000:
		return f"{value // 1000}k"
	return f"{value}"


def search_string(base_l, data):
	"""Generate a string used for searching"""
	return ', '.join([base_l] + [x[0].lower() for x in data])


def gen_images(base_l, data, show_10):
	"""Generate a series of images"""
	return ''.join(f'<span class="container{" hidden_class" if x[1] < show_10 else ""}" data-value="{x[1]}" data-search="{base_l}, {x[0].lower()}"><img src="{x[2]}" alt="{x[0]}" title="{x[0]}" class="item_icon" loading="lazy"><span class="bottom-right">{simple_format(x[1])}</span></span>' for x in data)


def gen_missing_images(data):
	"""Generate a series of images"""
	return ''.join(f'<span class="missing_span"><img src="{x[1]}" alt="{x[0]}" title="{x[0]}" class="item_icon" loading="lazy"></span>' for x in data)


def render_guide(show_10, unique_data, missing_data):
	file_loader = FileSystemLoader('templates')
	env = Environment(loader=file_loader)

	# set up helper functions
	env.filters['search_string'] = search_string
	env.filters['gen_images'] = gen_images
	env.filters['gen_missing_images'] = gen_missing_images

	template = env.get_template('index.html.jinja')

	keys = {
		'UniqueJewel': 'Exceptional Broken Circle Artifact',
		'UniqueWeapon': 'Greater Broken Circle Artifact',
		'UniqueArmour': 'Lesser Broken Circle Artifact',
		'UniqueAccessory': 'Grand Broken Circle Artifact'
	}

	for league in unique_data:
		# set up tables
		table_data = {keys[k]: defaultdict(list) for k in keys}
		for basetype in sorted(unique_data[league]):
			key = keys[unique_data[league][basetype][0][3]]
			table_data[key][basetype] = unique_data[league][basetype]

		missing_count = sum(1 for base in missing_data[league] for _ in missing_data[league][base])
		missing_data_sorted = {base: sorted(missing_data[league][base], key=lambda x: x[0]) for base in sorted(missing_data[league])}
		output = template.render(
			softcore='sc' in league,
			league=league,
			show_10=show_10[league],
			unique_data=table_data,
			update=datetime.now().strftime("%Y/%m/%d, %H:%M"),
			missing_count=missing_count,
			missing=missing_data_sorted
		)

		minified = minify(output)
		with open(f"docs/index{f'_{league}' if league != 'sct' else ''}.html", 'w', encoding='utf-8') as f:
			f.write(minified)
