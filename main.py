from browser import document as doc
from browser import bind


# Function for saving changes
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


del doc['loading']