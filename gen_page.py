from browser import document as doc
from browser.html import TABLE, TR, TH, TD, INPUT, SELECT, OPTION, DIV, BUTTON, SPAN, LI, H2, H3, IMG, COLGROUP, COL, P, SECTION, BR
from json import load


# Create the static elements of the home page
def init_page():
	min_val = INPUT(Type='number', min='0', step="1", value='0', Id="chaos_filter", Class='save')
	doc['show_hide'] <= DIV("Minimum Chaos Value to Show:" + min_val)
	t = TABLE(TR(TH("Selected") + TH("Base") + TH("Item(s)")), Class="borders")
	with open('unique.json') as f:
		data = load(f)

	for base in data:
		v = (DIV(IMG(src=x[2], alt=x[0], title=x[0], Class='item_icon') + DIV(x[1], Class='bottom-right'), Class='container') for x in data[base])
		t <= TR(TD(INPUT(Id=f"check-{base}", type='checkbox', data_id=f"check-{base}", Class='save')) + TD(base) + TD(v), data_id=data[base][0][0], data_value=data[base][0][1])

	doc['items'] <= t


init_page()
doc['loading'] <= DIV(Id='prerendered')
