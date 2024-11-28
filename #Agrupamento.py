#Agrupamento função crosstab e groupby
import pandas as pd
import numpy as np  

df = pd.read_excel("C:/Users/ulyss/OneDrive/Área de Trabalho/Curso Pós Graduação em Analise de Dados/PythonEstatistics/workplace.xlsx")
df1 = pd.crosstab(df['Sku'], df['V_Compra'], values=df.Qtd, aggfunc=(np.sum), margins=True)
print(df1)
df['valor_total'] = df.Qtd * df.V_Venda
print(df)
df2 = pd.crosstab(df['Sku'], df['V_Compra'], normalize='index').round(4)*100
print(df2)

df4 = df.groupby('Sku')

print(df.groupby('Sku').groups)
print(df.groupby('Sku').ngroups)
print(df.groupby('Sku').size())
print(df.groupby('Sku').get_group('Caneta'))
print(df.groupby('Sku').mean())
df.groupby(['Sku', 'V_Compra'])['V_Venda'].sum()


df_merge = pd.merge(Sku, V_Compra, how'inner', on='id')
print(df_merge)

