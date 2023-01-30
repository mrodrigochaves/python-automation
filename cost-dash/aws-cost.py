import matplotlib.pyplot as plt
import pandas as pd

# Carregue o arquivo .csv usando pandas
data = pd.read_csv("costs.csv")

# Selecione a coluna Total costs($) e as datas como x
x = data['Service']
y = data['Total costs($)']

# Plot o gráfico de barras
plt.bar(x, y)

# Adicione rótulos aos eixos x e y
plt.xlabel('Service')
plt.ylabel('Total costs($)')

# Exiba o gráfico
plt.show()
