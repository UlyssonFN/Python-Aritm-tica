#Dados com Pandas
import yfinance as yf #biblioteca de finacas
import pandas as pd #biblioteca de manipulacao de dados

acao = yf.Ticker('PETR4.SA')  #variavel acao recebe a busca
data = acao.history(period='5d') #variavel data recebe o histórico dentro da acao de acordo com o período
print(data) #demonstra na tela os dados

df = data.filter(items=['Open', 'Close']) #variavel df faz o filtro na coluna Open
print(df) #demonstra na tela os dados

df2 = data[(data.index > '2024-11-19')] #filtra a partir de uma condição
print(df2)#demonstra na tela os dados

#Outra formula de filtro
df3 = data.Close
df4 = data['Close']
df5 = data[['Close', 'Open']] 
df6 = data.index
print(df3, df4, df5, df6)

#comando retirar linhas comando Drop (axis=0 é linha 1 é coluna) 
df = data.drop(['2024-11-22', '2024-11-21'], axis=0)
df = data.drop(['High'], axis=1)
print(df)

#comandos de substituição Map e Reduce
df['new_dividens'] = data['Dividends'].map({0:2.99})
print(df)

df = data.drop(['Open', 'Low'], axis =1)
df['new_dividens2'] = data['Dividends'].map({0:3.00}).where(data.index == 
'2024-11-22')
print(df)