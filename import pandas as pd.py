import pandas as pd
#importa arquivo de banco de dados
df = pd.read_excel("C:/Users/ulyss/OneDrive/Área de Trabalho/Curso Pós Graduação em Analise de Dados/PythonEstatistics/workplace.xlsx")

print(df)
print(round(df.describe(),2)) #printa resultado com análise geral por coluna
#busca coluna com o filtro igual a Tinta
df2 = df[df['Sku'] == 'Tinta']
print(df2)
#Subistitui na coluna Sku o dado Tinta por Esmalte
df2['Sku'] = df2['Sku'].replace('Tinta', 'Esmalte')
print(df2)

df_missing = pd.DataFrame({'A' : [0,1,2,None,4],
                           'B' : [5,6,None,8,9],
                           'C' : ['a','b','a','a',None]})

print(df_missing.isnull().sum())
media = df_missing['A'].mean()
df_missing = df_missing['A'].fillna(media)
print(df_missing)

