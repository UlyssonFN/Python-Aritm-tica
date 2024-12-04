import pandas as pd

df = pd.read_csv("http://bit.ly/kaggletrain")
print(df)
#Seleciona uma columa de Sex para pegar os valores de homem e mulher
dummies = pd.get_dummies(df.Sex)
emb = pd.get_dummies(df.Embarked)
#Concatena dois dataframes criado do df original
df1 = pd.concat([dummies, emb], axis= 1)
#Converte os valores para inteiro pois estavam boleanos. 
print(df1.astype(int))
#Conta os valores verdadeiros.
print(df1.value_counts())

#Retira a coluna principal
#dummies = pd.get_dummies(df, columns=['Sex'], drop_first=True)





