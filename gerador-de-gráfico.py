from matplotlib import pyplot as plt 
import numpy as np

# Valores da biomassa em quilos (kg)
tipos_energeticos = ['5', '15', '25', '35']

# Valores da energia gerada por cada quantidade de biomassa em watt hora (Wh)
valores_energeticos = [4250, 12750, 21250, 29750]

# Definição das barras do gráfico 
plt.bar(tipos_energeticos, valores_energeticos, color = 'deepskyblue')

# Inserção dos valores da biomassa no eixo das abcissas 
plt.xticks(tipos_energeticos)

# Inserção de um texto de referência no eixo das ordenadas
plt.ylabel('Quantidade de Energia (Wh)')

# Inserção de um texto de referência no eixo das abscissas
plt.xlabel('Quantidade de Celulose (kg)')

# Inserção do titulo do gráfico
plt.title('Quantidade de Energia Gerada com Celulose')

# Inserção da grade horizontal do gráfico 
plt.grid(axis = 'y', linestyle = 'dotted')

# Plotagem do gráfico
plt.show()