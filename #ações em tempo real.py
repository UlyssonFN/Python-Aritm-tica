#ações em tempo real
import yfinance as yf

ticker = yf.Ticker('TSLA34.SA')
df = ticker.history(period='1y')
print(round((df),2))
print(round(df.describe(),2))