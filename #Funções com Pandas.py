#Funções com Pandas
import pandas as pd

#função de duplicar valores de uma coluna
def duplica_valores(rows):
    duplica = rows * 2
    return duplica

#Busca um BD
df_loja = pd.read_excel("C:/Users/ulyss/OneDrive/Área de Trabalho/Curso Pós Graduação em Analise de Dados/PythonEstatistics/workplace.xlsx")
#contagem de itens unicos de Sku
print(df_loja['Sku'].value_counts())
#Ver o máximo de linhas
pd.set_option('display.max_rows', 1000) 
#tras o valor mais caro dentro do campo qtd
print(df_loja['Qtd'].max()) 
#Separa colunas por grupo e agrega com base na média e organiza com base na média da coluna Sku
print(df_loja.groupby(['Sku','Qtd', 'V_Compra'])['V.Venda'].agg(['mean']).sort_values(by=['Sku','mean'])) 

#aplica função para duplicar coluna Qtd de acordo com a função definida
df_loja['Duplicar_Qtd'] = df_loja['Qtd'].apply(duplica_valores) 
#Todo valor que não tiver nada recebe o valor 0 para não ficar NaN
df_loja['Duplicar_Qtd'] = df_loja['Qtd'].fillna(0) 
print(df_loja)

#função lambda anônima, utilizado para pequenas linhas
df_loja['nova_coluna_lambda'] = df_loja['Qtd'].apply(lambda x: x * 2)
print(df_loja)

