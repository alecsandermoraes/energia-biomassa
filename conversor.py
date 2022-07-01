import PySimpleGUI as sg 
import sys

# Definição do tema escuro da interface 
sg.theme('Black')

# Criação do layout da interface 
layout = [
	[sg.Text('Insira um valor energético (Wh, kWh, J, kJ, cal, kCal)')],
	[sg.Input(key = 'value')],
	[sg.Button('Converter')]
]

# Criação da janela de acordo com o layout 
window = sg.Window('Conversor de Valores Energéticos', layout)

# Início do loop que manterá o programa aberto 
while True:
	try:
		# Captura dos eventos e valores 
		events, values = window.read()
		# Verificação do evento de fechamento, se for o caso, janela fecha
		if events == sg.WIN_CLOSED:
			window.close()
		# Verificação do valor passado, se for vazio, aparecerá um pop-up
		if values['value'] == '':
			sg.popup('Não foi inserido nenhum valor energético!')
			continue
		try:
			# Definição da mensagem que mostrará os valores 
			r = """Os valores convertidos são:
{}Wh
{}kWh
{}J
{}kJ
{}cal
{}kCal"""
			value = values['value']
			# Verificação: Se o valor passado é em watt hora (Wh) ou não
			if value.endswith('Wh') and not 'k' in value:
				valuelist = []
				# Captura dos dígitos 
				for c in value:
					if c.isdigit():
						valuelist.append(c)
				# Filtragem da informação
				value = str(valuelist).replace('[', '').replace(',', '').replace(' ', '').replace(']', '').replace("'", '')
				value = int(value)
				# Conversão para outros valores energéticos  
				kwh = value / 1000
				j = kwh * 3.6e+6
				kj = j / 1000
				cal = kj * 239 
				kcal = cal / 1000
				# Inserção dos valores na mensagem
				r = r.format(value, kwh, j, kj, cal, kcal)
				# Pop-up mostrando a mensagem com os resultados 
				sg.popup(r)
			# Verificação: Se o valor é em quilowatt hora (kWh) ou não
			elif value.endswith('kWh'):
				valuelist = []
				# Captura dos dígitos 
				for c in value:
					if c.isdigit():
						valuelist.append(c)
				# Filtragem da informação 
				value = str(valuelist).replace('[', '').replace(',', '').replace(' ', '').replace(']', '').replace("'", '')
				value = int(value)
				# Conversão para outros valores energéticos 
				j = value * 3.6e+6
				kj = j / 1000 
				cal = kj * 239
				kcal = cal / 1000
				wh = value * 1000 
				# Inserção dos resultados na mensagem 
				r = r.format(wh, value, j, kj, cal, kcal)
				# Apresentação dos resultados 
				sg.popup(r)
			# Verificação: Se o valor é em joule (J) ou não 
			elif value.endswith('J') and not 'k' in value:
				valuelist = []
				# Captura dos dígitos 
				for c in value:
					if c.isdigit():
						valuelist.append(c)
				# Filtragem da informação 
				value = str(valuelist).replace('[', '').replace(',', '').replace(' ', '').replace(']', '').replace("'", '')
				value = int(value)
				# Conversão para outros valores energéticos
				kj = value / 1000 
				cal = kj * 239 
				kcal = cal / 1000 
				wh = kj / 3.6
				kwh = wh / 1000
				# Inserção dos resultados na mensagem 
				r = r.format(wh, kwh, value, kj, cal, kcal)
				# Apresentação dos resultados 
				sg.popup(r)
			# Verificação: Se o valor é quilojoule (kJ) ou não 
			elif value.endswith('kJ'):
				valuelist = []
				# Captura dos dígitos 
				for c in value:
					if c.isdigit():
						valuelist.append(c)
				# Filtragem da informação 
				value = str(valuelist).replace('[', '').replace(',', '').replace(' ', '').replace(']', '').replace("'", '')
				value = int(value)
				# Conversão para outros valores energéticos
				cal = value * 239 
				kcal = cal / 1000
				wh = kcal / 1.162 
				kwh = wh / 1000
				j = kwh * 3.6e+6
				# Inserção dos resultados na mensagem 
				r = r.format(wh, kwh, j, value, cal, kcal)
				# Apresentação dos resultados 
				sg.popup(r)
			# Verificação: Se o valor é caloria (cal) ou não
			elif value.endswith('cal') and not 'k' in value:
				valuelist = []
				# Captura dos dígitos
				for c in value:
					if c.isdigit():
						valuelist.append(c)
				# Filtragem da informação
				value = str(valuelist).replace('[', '').replace(',', '').replace(' ', '').replace(']', '').replace("'", '')
				value = int(value)
				# Conversão para outros valores energéticos
				kcal = value / 1000
				j = kcal * 4184
				kj = j / 1000
				kwh = value / 860421
				wh = kwh * 1000
				# Inserção dos resultados na mensagem
				r = r.format(wh, kwh, j, kj, value, kcal)
				# Apresentação dos resultados 
				sg.popup(r)
			# Verificação: Se o valor é em quilocaloria (kCal) ou não
			elif value.endswith('kCal'):
				valuelist = []
				# Captura dos dígitos 
				for c in value:
					if c.isdigit():
						valuelist.append(c)
				# Filtragem da informação 
				value = str(valuelist).replace('[', '').replace(',', '').replace(' ', '').replace(']', '').replace("'", '')
				value = int(value)
				# Conversão para outros valores energéticos 
				j = value * 4184 
				cal = value * 1000 
				kj = j / 1000 
				wh = kj / 3.6 
				kwh = wh / 1000 
				# Inserção dos resultados na mensagem
				r = r.format(wh, kwh, j, kj, cal, value)
				# Apresentação dos resultados 
				sg.popup(r)
			# Verificação: Se o valor é inválido 
			else:
				sg.popup('O valor deve ser inserido e seu tipo energético logo em seguida (Wh, kWh, J, kJ, cal, kCal)!')
				continue
		except TypeError:
			break
	except TypeError:
		break

sys.exit()