import PySimpleGUI as sg 
import sys

# Definição do tema escuro da interface 
sg.theme('Black')

# Criação do layout 
layout = [
    [sg.Text('Possuindo um valor de referência de algum outro local, insira a quantidade de energia produzida por 1 quilo\nda biomassa e, logo após, a quantidade da biomassa que deseja saber o quanto de energia será gerada')],
    [sg.Text('Energia Liberada por um 1kg de Biomassa (Wh):'), sg.Input(key = 'energia')],
    [sg.Text('Quantidade de Biomassa Desejada (kg):'), sg.Input(key = 'biomassa')],
    [sg.Button('Calcular')],
]

# Criação da janela de acordo com o layout criado 
window = sg.Window('Cálculo de Energia a Biomassa', layout)

# Início do loop que manterá o programa aberto 
while True:
    try:
        # Captura dos eventos e valores da interface
        events, values = window.read()
        # Verificação se o evento é fechar o programa, se sim, janela fecha
        if events == sg.WIN_CLOSED:
            window.close()
        # Verificação do valor, se ele for vazio, aparecerá um pop-up
        if values['energia'] == '' or values['biomassa'] == '':
            sg.popup('Não foi possível calcular, pois os campos não foram preenchidos')
            continue
        try:
            # Cálculo da energia com o valor de biomassa entregue
            result = int(values['energia']) * int(values['biomassa'])
            # Apresentação do resultado em quilojoule (kJ)
            sg.popup(f'{int(values["biomassa"])} kg de biomassa irá gerar: ' + str(result) + ' Wh de energia')
        except ValueError:
            # Verificação se o valor entregue é válido
            sg.popup('Insira apenas números como valores')
            continue
        except TypeError:
            break
    except TypeError:
        break

sys.exit()