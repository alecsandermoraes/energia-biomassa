import PySimpleGUI as sg 
import sys

sg.theme('Black')

layout = [
	[sg.Text('Insira um valor energético (Wh, kWh, J, kJ, cal, kCal)')],
	[sg.Input(key = 'value')],
	[sg.Button('Converter')]
]

window = sg.Window('Conversor de Valores Energéticos', layout)

while True:
	try:
		events, values = window.read()
		if events == sg.WIN_CLOSED:
			window.close()
		if values['value'] == '':
			sg.popup('Não foi inserido nenhum valor energético!')
			continue
		try:
			r = """Os valores convertidos são:
{}Wh
{}kWh
{}J
{}kJ
{}cal
{}kCal"""
			value = values['value']
			if value.endswith('Wh') and not 'k' in value:
				valuelist = []
				for c in value:
					if c.isdigit():
						valuelist.append(c)
				value = str(valuelist).replace('[', '').replace(',', '').replace(' ', '').replace(']', '').replace("'", '')
				value = int(value)     
				kwh = value / 1000
				j = kwh * 3.6e+6
				kj = j / 1000
				cal = kj * 239 
				kcal = cal / 1000
				r = r.format(value, kwh, j, kj, cal, kcal)
				sg.popup(r)
			elif value.endswith('kWh'):
				valuelist = []
				for c in value:
					if c.isdigit():
						valuelist.append(c)
				value = str(valuelist).replace('[', '').replace(',', '').replace(' ', '').replace(']', '').replace("'", '')
				value = int(value)
				j = value * 3.6e+6
				kj = j / 1000 
				cal = kj * 239
				kcal = cal / 1000
				wh = value * 1000 
				r = r.format(wh, value, j, kj, cal, kcal)
				sg.popup(r)
			elif value.endswith('J') and not 'k' in value:
				valuelist = []
				for c in value:
					if c.isdigit():
						valuelist.append(c)
				value = str(valuelist).replace('[', '').replace(',', '').replace(' ', '').replace(']', '').replace("'", '')
				value = int(value)
				kj = value / 1000 
				cal = kj * 239 
				kcal = cal / 1000 
				wh = kj / 3.6
				kwh = wh / 1000
				r = r.format(wh, kwh, value, kj, cal, kcal)
				sg.popup(r)
			elif value.endswith('kJ'):
				valuelist = []
				for c in value:
					if c.isdigit():
						valuelist.append(c)
				value = str(valuelist).replace('[', '').replace(',', '').replace(' ', '').replace(']', '').replace("'", '')
				value = int(value)
				cal = value * 239 
				kcal = cal / 1000
				wh = kcal / 1.162 
				kwh = wh / 1000
				j = kwh * 3.6e+6
				r = r.format(wh, kwh, j, value, cal, kcal)
				sg.popup(r)
			elif value.endswith('cal') and not 'k' in value:
				valuelist = []
				for c in value:
					if c.isdigit():
						valuelist.append(c)
				value = str(valuelist).replace('[', '').replace(',', '').replace(' ', '').replace(']', '').replace("'", '')
				value = int(value)
				kcal = value / 1000
				j = kcal * 4184
				kj = j / 1000
				kwh = value / 860421
				wh = kwh * 1000 
				r = r.format(wh, kwh, j, kj, value, kcal)
				sg.popup(r)
			elif value.endswith('kCal'):
				valuelist = []
				for c in value:
					if c.isdigit():
						valuelist.append(c)
				value = str(valuelist).replace('[', '').replace(',', '').replace(' ', '').replace(']', '').replace("'", '')
				value = int(value)
				j = value * 4184 
				cal = value * 1000 
				kj = j / 1000 
				wh = kj / 3.6 
				kwh = wh / 1000 
				r = r.format(wh, kwh, j, kj, cal, value)
				sg.popup(r)
			else:
				sg.popup('O valor deve ser inserido e seu tipo energético logo em seguida (Wh, kWh, J, kJ, cal, kCal)!')
				continue
		except TypeError:
			break
	except TypeError:
		break

sys.exit()