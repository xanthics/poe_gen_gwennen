from browser import document as doc
from browser import bind, worker
from ngram_generated import ngrams, subnames
from browser.html import P, BR


myWorker = worker.Worker("myworker")


# Function handling filtering changes
@bind('.save', 'change')
def save_state(ev):
	if ev.target.id == 'chaos_filter':
		c = True if doc['hide_low_value'].value == 'hide' else False
		for el in doc.get(selector="[data-value]"):
			if int(el.attrs['data-value']) >= int(ev.target.value):
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
	elif ev.target.id == 'hide_low_value':
		c = True if doc['hide_low_value'].value == 'hide' else False
		value = int(doc['chaos_filter'].value)
		for el in doc.get(selector="div[data-value]"):
			if c:
				if int(el.attrs['data-value']) >= value:
					if 'container' in el.class_name:
						el.attrs['class'] = "container"
				else:
					el.attrs['class'] = "container hidden_class"
			else:
				el.attrs['class'] = "container"


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


doc["generate"].bind("click", generate_string)
doc["select_visible"].bind("click", select_visible)
del doc['loading']