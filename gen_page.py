from browser import document as doc
from browser.html import TABLE, TR, TH, TD, INPUT, SELECT, OPTION, DIV, BUTTON, SPAN, LI, H2, H3, IMG, COLGROUP, COL, P, SECTION, BR, STRONG, HR, UL
from json import load
from last_update import time


# Create the static elements of the home page
def init_page():
	# header
	doc['time'].text = f"poe.ninja data last updated at {time} PST"
	# help
	help_file = SECTION(Id="help")
	help_file <= P("This page generates simple regex search strings that are compatible with Path of Exile.  It uses price data from poe.ninja to present an initial selection that you can then personalize by changing the search filters and changing which item bases are selected.  This tool does a lot of work behind the scene to generate compact search strings while staying within PoE's character limit.")

	help_file <= HR()

	help_file <= P("Atlas bases are available to select via 'Influenced Base', they have chaos value set to 0.")

	help_file <= HR()

	help_file <= P("Default Minimum Chaos is initialized to show 10 bases for the current league.  If you would like to select other bases, use the selection filters to change what is visible.")
	help_file <= P(STRONG("Keyword(s) search") + " overrides all other filter settings.  Clear keyword search to use them.  Search can display an empty row if it's the combination of two or more uniques on a base that matches the search terms.  EG 'gold rim' will show Viridian Jewel base because 2 separate uniques partially match the search.")

	help_file <= P("Clicking " + STRONG("Generate String") + " will generate search strings based on all selected rows.  This can cause many calculations and may take a bit to return a result")
	help_file <= P("Due to limitations on the size of the search box in game you may be given more than 1 search string.  If this happens you have 2 choices.")

	ul = UL()
	ul <= LI("Remove some items that you are looking for until the string is short enough.")
	ul <= LI("Paste each line for each page of items. Awakened PoE Trade, or win 10 multi-clipboard(built in) make it a lot less painful.")
	help_file <= ul

	help_file <= HR()

	help_file <= P(STRONG("Select Matching Only") + " selects only rows that match current Keyword(s) Search or Minimum Chaos settings and deselects all others.")
	help_file <= P(STRONG("Select Visible") + " adds all rows that match current Keyword(s) Search or Minimum Chaos to current selection.")
	help_file <= P(STRONG("Clear Selected") + " deselects all rows.")
	doc['helpsection'] <= BUTTON("Show Help and About", Id='toggle_help') + help_file
	# regex result
	doc['regex_box'] <= DIV(BUTTON("Generate String", Id='generate'))
	doc['regex_box'] <= DIV("No strings generated yet.", Id="generated_strings", Class='sec_div grind')
	# selected
	cst = SELECT(Id=f"hide_low_value", Class=f"save onehundred")
	for s in ['hide', 'show']:
		cst <= OPTION(s.capitalize(), value=s)
	always_show = SELECT(Id=f"always_show", Class=f"save onehundred")
	for s in ['show', 'hide']:
		always_show <= OPTION(s.capitalize(), value=s)
	min_val = INPUT(Type='number', min='0', step="1", value='20', Id="chaos_filter", Class='save')
	t = TABLE(TR(TH() + TH('Selection')))
	t <= TR(TD("Always show selected rows:", Class="right_text") + TD(always_show))
	t <= TR(TD("Show low value items in row:", Class="right_text") + TD(cst))
	t <= TR(TD("Minimum Chaos value to show:", Class="right_text") + TD(min_val))
	t <= TR(TD("Keyword(s) Search:", Class="right_text") + TD(INPUT(Type='text', Id="keywords", Class='save') + BUTTON('x', Id='clear_keywords')))
	doc['show_hide'] <= t + BR()
	# item table buttons
	doc['show_hide'] <= DIV(BUTTON("Select Matching Only", Id='select_matching'))
	doc['show_hide'] <= DIV(BUTTON("Select Visible", Id='select_visible'))
	doc['show_hide'] <= DIV(BUTTON("Clear Selected", Id='clear_selected'))

	# Load and display league specific unique data
	t = TABLE(TR(TH("Selected", Class='col_1') + TH("Base", Class='col_2') + TH("Item(s)")), Class="borders onehundred")
	with open(f'{doc.query.getvalue("league", "sc")}_unique.json') as f:
		data = load(f)
	for base in data:
		base_l = base.lower()
		v = (SPAN(IMG(src=x[2], alt=x[0], title=x[0], Class='item_icon', loading="lazy") + SPAN(x[1], Class='bottom-right'), Class='container', data_value=x[1], data_search=f"{base_l}, {x[0].lower()}") for x in data[base])
		searchstring = ', '.join([base_l] + [x[0].lower() for x in data[base]])
		t <= TR(TD(INPUT(Id=f"check-{base_l.replace(' ', '_')}", type='checkbox', data_id=base_l, Class='save')) + TD(base) + TD(v), data_id=base_l, data_value=data[base][0][1], data_search=searchstring)

	doc['items'] <= t


init_page()
doc['loading'] <= DIV(Id='prerendered')
