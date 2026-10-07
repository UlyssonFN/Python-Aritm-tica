import pandas as pd
import matplotlib.pyplot as plt

# Carregando base
df = pd.read_csv(r"C:\Users\ulyss\OneDrive\Área de Trabalho\Live Linkedin\Aula Udemy\dados_enem_2021_BA.csv")

# Médias
public = df.query('TP_ESCOLA == 2').NU_NOTA_MT.mean()
partic = df.query('TP_ESCOLA == 3').NU_NOTA_MT.mean()

print("Média Pública:", round(public, 2))
print("Média Particular:", round(partic, 2))

if public > partic:
    print("Nota da Escola Pública é maior que a Particular")
    print("Diferença de:", round(public - partic, 2), "pontos")
else:
    print("Nota da Escola Particular é maior que a Pública")
    print("Diferença de:", round(partic - public, 2), "pontos")

# Criando dataframe só com escolas públicas e particulares
df_filtrado = df.query('TP_ESCOLA == 2 or TP_ESCOLA == 3')

# -------- Gráfico 1: Distribuição (Boxplot) --------
df_filtrado.boxplot(column='NU_NOTA_MT', by='TP_ESCOLA')
plt.title('Distribuição das notas de Matemática por tipo de escola')
plt.suptitle('')  # remove título duplicado
plt.xlabel('2 = Pública | 3 = Particular')
plt.ylabel('Nota de Matemática')
plt.show()

# -------- Gráfico 2: Médias (Barras) --------
medias = {'Escola Pública': public, 'Escola Particular': partic}

plt.bar(medias.keys(), medias.values())
plt.title('Média das notas de Matemática por tipo de escola')
plt.ylabel('Nota Média')
plt.show()