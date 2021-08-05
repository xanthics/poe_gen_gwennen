from browser import document as doc
from browser.html import TABLE, TR, TH, TD, INPUT, SELECT, OPTION, DIV, BUTTON, SPAN, LI, H2, H3, IMG, COLGROUP, COL, P, SECTION, BR
from json import load


# Create the static elements of the home page
def init_page():
	t = TABLE(TR(TH("Selected") + TH("Base") + TH("Item(s)")), Class="borders")
	with open('unique.json') as f:
		data = load(f)

	for base in data:
		v = (DIV(IMG(src=x[2], alt=x[0], title=x[0], Class='item_icon') + DIV(x[1], Class='bottom-right'), data_id=data[base][0][0], Class='container') for x in data[base])
		t <= TR(TD(INPUT(Id=f"check-{base}", type='checkbox', data_id=f"check-{base}", Class='save')) + TD(base) + TD(v))

	doc['items'] <= t


init_page()
doc['loading'] <= DIV(Id='prerendered')
