#Engenharia de Recursos
import pandas as pd

#importação de base de dados
df = pd.read_excel("C:/Users/ulyss/OneDrive/Área de Trabalho/Curso Pós Graduação em Analise de Dados/PythonEstatistics/workplace.xlsx")

#filtro de 10 na coluna quantidade
#df_qtd = df[df['Qtd'] == 10]

#verifica os tipos de valores de cada campo
df_qtd = df.copy()

#Realizar a conversão da coluna Sku para string
df_qtd['Sku'] = df_qtd['Sku'].astype(str)
#cria uma nova coluna com base na venda de 2 dias puxando a média para baixo
df_qtd['Criando_Coluna'] = df_qtd['V_Venda'].rolling(2).mean()
#print(df_qtd.dtypes)
#retira colunas desnecessárias
features = df_qtd.drop(['V_Compra', 'Cod'], axis= 1)
print(features)
