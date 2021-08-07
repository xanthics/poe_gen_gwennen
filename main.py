from browser import document as doc
from browser import bind, worker
from browser.html import P, BR, INPUT


myWorker = worker.Worker("myworker")


# Function handling filtering changes
@bind('.save', 'change')
def save_state(ev):
	if ((ev.target.id in ['chaos_filter', 'hide_low_value', 'always_show'] or ev.target.type == 'checkbox') and not doc['keywords'].value) or (ev.target.id == 'keywords' and not ev.target.value):
		always_show = True if doc['always_show'].value == 'show' else False
		hide_low = True if doc['hide_low_value'].value == 'hide' else False
		value = int(doc['chaos_filter'].value)
		for el in doc.get(selector="[data-value]"):
			if int(el.attrs['data-value']) >= value or (always_show and 'container' not in el.class_name and doc[f'check-{el.attrs["data-id"].replace(" ", "_")}'].checked):
				if 'hidden_class' in el.class_name:
					el.attrs['class'] = "container"
				elif 'hidden' in el.attrs:
					del el.attrs['hidden']
			else:
				if 'container' in el.class_name:
					if hide_low:
						el.attrs['class'] = "container hidden_class"
					else:
						el.attrs['class'] = "container"
				else:
					el.attrs['hidden'] = ''
	elif ev.target.id == 'keywords':
		search_terms = ev.target.value.lower().split()
		for el in doc.get(selector="[data-search]"):
			terms = el.attrs['data-search']
			if all(x in terms for x in search_terms):
				if 'hidden_class' in el.class_name:
					el.attrs['class'] = "container"
				elif 'hidden' in el.attrs:
					del el.attrs['hidden']
			else:
				if 'container' in el.class_name:
					el.attrs['class'] = "container hidden_class"
				else:
					el.attrs['hidden'] = ''


@bind(myWorker, 'message')
def onmessage(evt):
	if evt.data[0] == 'overlap':
		doc['generated_strings'] <= P(f"{evt.data[1]} will also match {evt.data[2]} due to being an unavoidable substring match")
	elif evt.data[0] == 'done':
		if evt.data[1]:
			del doc['updates']
			# input size uses 'M' * size to figure out width.  Only correct with fixed width font.
			doc['generated_strings'] <= (P(f'{c}: ' + INPUT(value=x, size=len(x)+1, readonly='', Class='monospace', type="text", Id=f"{c}_search", onClick=f'document.getElementById("{c}_search").select(); document.execCommand("copy");')) for c, x in enumerate(evt.data[1], start=1))
	elif evt.data[0] == 'update':
		doc['updates'].text = evt.data[1]
	elif evt.data[0] == 'debug':
		# print(evt.data[1])
		pass


def select_visible(ev):
	for el in doc.get(selector="tr[data-id]"):
		check_id = f'check-{el.attrs["data-id"].replace(" ", "_")}'
		if 'hidden' in el.attrs:
			doc[check_id].checked = False
		else:
			doc[check_id].checked = True


def generate_string(ev):
	doc['generated_strings'].text = ''
	good_bases = []
	for el in doc.get(selector="input[type=checkbox]"):
		if el.checked:
			good_bases.append(el.attrs['data-id'])

	if good_bases:
		doc['generated_strings'] <= P('Starting web worker', Id='updates')
		myWorker.send(("init", good_bases))
	else:
		doc['generated_strings'] <= P("No bases were selected, so no result to return.")


# Set the initial page state
def init_page():
	value = int(doc['chaos_filter'].value)
	c = True if doc['hide_low_value'].value == 'hide' else False
	for el in doc.get(selector="[data-value]"):
		if int(el.attrs['data-value']) >= value:
			if 'container' in el.class_name:
				el.attrs['class'] = "container"
			elif 'hidden' in el.attrs:
				del el.attrs['hidden']
		else:
			if 'container' in el.class_name:
				if c:
					el.attrs['class'] = "container hidden_class"
			else:
				el.attrs['hidden'] = ''
	select_visible(None)


doc["generate"].bind("click", generate_string)
doc["select_visible"].bind("click", select_visible)
init_page()
del doc['loading']
