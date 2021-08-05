from browser import document as doc
from browser import bind


# Function for saving changes
@bind('.save', 'change')
def save_state(ev):
	if ev.target.id == 'chaos_filter':
		print(ev.target.id, ev.target.value)
		for el in doc.get(selector="tr[data-value]"):
			print(el)
			if int(el.attrs['data-value']) >= int(ev.target.value):
				if 'hidden' in el.attrs:
					del el.attrs['hidden']
			else:
				el.attrs['hidden'] = ''


del doc['loading']