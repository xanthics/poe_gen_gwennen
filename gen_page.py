from browser import document as doc
from browser.html import TABLE, TR, TH, TD, INPUT, SELECT, OPTION, DIV, BUTTON, SPAN, LI, H2, H3, IMG, COLGROUP, COL, P, SECTION, BR
from json import load


# Create the static elements of the home page
def init_page():
	# selected
	cst = SELECT(Id=f"hide_low_value", Class=f"save onehundred")
	for s in ['show', 'hide']:
		cst <= OPTION(s.capitalize(), value=s)
	min_val = INPUT(Type='number', min='0', step="1", value='0', Id="chaos_filter", Class='save onehundred')
	t = TABLE(TR(TH() + TH('Selection')))
	t <= TR(TD("Minimum Chaos value to show:") + TD(min_val))
	t <= TR(TD("Show low value items in row:") + TD(cst))
	doc['show_hide'] <= t + DIV(BUTTON("Generate string", Id='generate') + "This will cause many calculations and may take a bit to return a result") + DIV("No strings generated yet.", Id="generated_strings", Class='sec_div grind') + BUTTON("Select All Visible Only", Id='select_visible')
	t = TABLE(TR(TH("Selected", Class='col_1') + TH("Base", Class='col_2') + TH("Item(s)")), Class="borders onehundred")
	with open('unique.json') as f:
		data = load(f)

	for base in data:
		base_l = base.lower()
		v = (DIV(IMG(src=x[2], alt=x[0], title=x[0], Class='item_icon') + DIV(x[1], Class='bottom-right'), Class='container', data_value=x[1]) for x in data[base])
		t <= TR(TD(INPUT(Id=f"check-{base_l.replace(' ', '_')}", type='checkbox', data_id=base_l, Class='save')) + TD(base) + TD(v), data_id=base_l, data_value=data[base][0][1])

	doc['items'] <= t


init_page()
doc['loading'] <= DIV(Id='prerendered')
