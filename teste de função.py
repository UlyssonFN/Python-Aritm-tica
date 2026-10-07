import pandas as pd
import numpy as np

def calculo():
   resultado = dinheiro * tempo
   print('A conclusão do tempo informado, você terá: ',resultado, 'R$')


dinheiro = float(input("Digite o valor que quer guardar: "))
tempo = int(input("Digite a quantidade de meses que quer guardar: "))

valores = {'janeiro': dinheiro, 'fevereiro': dinheiro, 'março': dinheiro, 'abril': dinheiro, 'maio': dinheiro, 'junho': dinheiro, 'julho': dinheiro, 'agosto': dinheiro, 'setembro': dinheiro, 'outubro': dinheiro, 'novembro': dinheiro, 'dezembro': dinheiro}
call = calculo()
df = {valores}
print(df.tolist())