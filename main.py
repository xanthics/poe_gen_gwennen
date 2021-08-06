from browser import document as doc
from browser import bind, worker
from ngram_generated import ngrams, subnames
from browser.html import P, BR


myWorker = worker.Worker("myworker")


# Function handling filtering changes
@bind('.save', 'change')
def save_state(ev):
	if ev.target.id in ['chaos_filter', 'hide_low_value']:
		c = True if doc['hide_low_value'].value == 'hide' else False
		value = int(doc['chaos_filter'].value)
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


@bind(myWorker, 'message')
def onmessage(evt):
	if evt.data[0] == 'overlap':
		doc['generated_strings'] <= P(f"{evt.data[1]} will also match {evt.data[2]} due to being an unavoidable substring match")
	elif evt.data[0] == 'done':
		if evt.data[1]:
			del doc['updates']
			doc['generated_strings'] <= (P(f'{c}: {x}') for c, x in enumerate(evt.data[1], start=1))
	elif evt.data[0] == 'update':
		doc['updates'].text = evt.data[1]


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


doc["generate"].bind("click", generate_string)
doc["select_visible"].bind("click", select_visible)
init_page()
del doc['loading']
