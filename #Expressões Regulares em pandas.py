#Expressões Regulares em pandas
import pandas as pd

df = pd.read_csv('C:/Users/ulyss/OneDrive/Área de Trabalho/Curso Pós Graduação em Analise de Dados/PythonEstatistics/Bovespa.csv', delimiter=";")

reg = df.filter(regex=".[_]")
df.replace('.34', '000', regex = True)


print(df)
