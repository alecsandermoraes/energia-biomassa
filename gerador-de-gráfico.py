from matplotlib import pyplot as plt 
import numpy as np

tipos_energeticos = ['5', '15', '25', '35']
valores_energeticos = [4250, 12750, 21250, 29750]

plt.bar(tipos_energeticos, valores_energeticos, color = 'deepskyblue')
plt.xticks(tipos_energeticos)
plt.ylabel('Quantidade de Energia (Wh)')
plt.xlabel('Quantidade de Celulose (kg)')
plt.title('Quantidade de Energia Gerada com Celulose')
plt.grid(axis = 'y', linestyle = 'dotted')

plt.show()