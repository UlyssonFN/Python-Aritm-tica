import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('C:/Users/ulyss/OneDrive/Área de Trabalho/Curso Pós Graduação em Analise de Dados/PythonEstatistics/weight-height.csv')
plt.hist(df.Weight, bins=30, rwidth=0.8)
plt.xlabel('Peso') #Nome do Eixo X
plt.ylabel('Frequência') #Nome do Eixo Y
plt.title('Histograma de Peso')

plt.show()

#Adiciona a coluna zscore onde calcula na coluna Weight - média de Weight / pelo desvio padrão de Weight
df['zscore'] = (df.Weight - df.Weight.mean()) / df.Weight.std()
print(df)
#Retornar os itens que estão com o desvio menor que -2 e maior que 2
df2 = df[(df.zscore < -2) | (df.zscore > 2)]
print(df2)