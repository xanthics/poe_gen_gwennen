from browser import document as doc
from browser.html import TABLE, TR, TH, TD, INPUT, SELECT, OPTION, DIV, BUTTON, SPAN, LI, H2, H3, IMG, COLGROUP, COL, P, SECTION, BR
from json import load
from last_update import time


# Create the static elements of the home page
def init_page():
	doc['time'].text = f"poe.ninja data last updated at {time} PST"
	# selected
	cst = SELECT(Id=f"hide_low_value", Class=f"save onehundred")
	for s in ['hide', 'show']:
		cst <= OPTION(s.capitalize(), value=s)
	always_show = SELECT(Id=f"always_show", Class=f"save onehundred")
	for s in ['show', 'hide']:
		always_show <= OPTION(s.capitalize(), value=s)
	min_val = INPUT(Type='number', min='0', step="1", value='20', Id="chaos_filter", Class='save')
	t = TABLE(TR(TH() + TH('Selection')))
	t <= TR(TD("Always show selected:", Class="right_text") + TD(always_show))
	t <= TR(TD("Minimum Chaos value to show:", Class="right_text") + TD(min_val))
	t <= TR(TD("Show low value items in row:", Class="right_text") + TD(cst))
	t <= TR(TD("Keyword(s) Search:", Class="right_text") + TD(INPUT(Type='text', Id="keywords", Class='save')))
	doc['show_hide'] <= t + P("Hit enter or click outside the inputs to update the page.")
	doc['show_hide'] <= P("Note that the keyword search overrides all other filter settings.  Clear keyword search to use them.  Search will display an empty row if it's the combination of the base + a unique that matches the search terms.  EG gold rim will show Viridian Jewel base because 2 separate uniques partially match the search.")
	doc['show_hide'] <= DIV(BUTTON("Generate String", Id='generate') + "This will cause many calculations and may take a bit to return a result")
	doc['show_hide'] <= DIV("No strings generated yet.", Id="generated_strings", Class='sec_div grind') + BUTTON("Select All Visible Only", Id='select_visible')

	# Load and display league specific unique data
	t = TABLE(TR(TH("Selected", Class='col_1') + TH("Base", Class='col_2') + TH("Item(s)")), Class="borders onehundred")
	with open(f'{doc.query.getvalue("league", "sc")}_unique.json') as f:
		data = load(f)
	for base in data:
		base_l = base.lower()
		v = (DIV(IMG(src=x[2], alt=x[0], title=x[0], Class='item_icon', loading="lazy") + DIV(x[1], Class='bottom-right'), Class='container', data_value=x[1], data_search=f"{base_l}, {x[0].lower()}") for x in data[base])
		searchstring = ', '.join([base_l] + [x[0].lower() for x in data[base]])
		t <= TR(TD(INPUT(Id=f"check-{base_l.replace(' ', '_')}", type='checkbox', data_id=base_l, Class='save')) + TD(base) + TD(v), data_id=base_l, data_value=data[base][0][1], data_search=searchstring)

	doc['items'] <= t


init_page()
doc['loading'] <= DIV(Id='prerendered')
