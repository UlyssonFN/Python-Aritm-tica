#Indice em Pandas
import pandas as pd

frutas = ['maça', 'banana', 'abacaxi']
#retorna o valor 0 até o valor 1, excluindo o valor 2.
print(frutas[0:2])
#retorna todo o indice
print(frutas)

#importa BD para trabalho
df_loja = pd.read_excel("C:/Users/ulyss/OneDrive/Área de Trabalho/Curso Pós Graduação em Analise de Dados/PythonEstatistics/workplace.xlsx")
#crio uma variável nova onde pegou o dataframe fez um filtro na coluna QTD tudo que contém 10
df_filtro = df_loja[df_loja['Qtd'] == 10]
#retorna o filtro feito acima
print(df_filtro)
#comando loc faz o filtro mediante a linha [9:16] quanto por coluna 'Sku'
df1 = df_filtro.loc[9:16,'Sku']
print(df1)
#quando o comando está : quer dizer que trará todas as linhas e o número 1 é referente a primeira coluna
df2 = df_filtro.iloc[:, 1]
print(df2)
#em resumo antes da virgula é linha e depois é coluna
df3 = df_filtro.iloc[0:4, :]
#Reseta o indice para começar com 0, o comando drop=True exclue o indice antigo, pois senão fizer isso ele gera uma coluna com o indice antigo
print(df3.reset_index(drop=True))
print(df_loja.reset_index(inplace=True, drop=True))

#muda a coluna indice de acordo com a coluna determinada dentro do set_index
df4 = df_filtro.set_index('Sku')
print(df4)



