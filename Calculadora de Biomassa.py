import PySimpleGUI as sg 
import sys

sg.theme('Dark')

layout = [
    [sg.Text('Possuindo um valor de referência de algum outro local, insira a quantidade de energia produzida por certa quantidade de biomassa')],
    [sg.Text('Quantidade de Biomassa (kg):'), sg.Input(key = 'biomassa')],
    [sg.Text('Energia Liberada (kJ):'), sg.Input(key = 'energia')],
    [sg.Button('Calcular')],
]


window = sg.Window('Cálculo de Energia a Biomassa', layout)

while True:
    events, values = window.read()
    if events == sg.WIN_CLOSED:
        window.close()
    if values['energia'] == '' or values['biomassa'] == '':
        sg.popup('Não foi possível calcular, pois os campos não foram preenchidos')
        continue
    try:
        result = (1 * int(values['energia'])) / int(values['biomassa'])
        sg.popup('1kg de biomassa irá gerar: ' + str(result) + 'kJ de energia')
    except ValueError:
        sg.popup('Insira apenas números como valores')
        continue
    except TypeError:
        break

sys.exit()