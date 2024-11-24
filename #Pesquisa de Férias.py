#Pesquisa de Férias
import pandas as pd
contar = 1
while contar == 1:
    try:
        matricula = int(input("Digite a Matricula para pesquisar o período das suas férias: "))
        df = pd.read_excel("C:/Users/ulyss/OneDrive/Área de Trabalho/Curso Pós Graduação em Analise de Dados/PythonEstatistics/Ferias.xlsx")
        df = df.drop(['Macro', 'Ano Saída', 'Mês Saída'], axis=1)
        df1 = df[df['Matricula'] == matricula]
        print(df1)
        resp = str(input("Deseja pesquisar uma nova férias? (Sim/Não) ")).lower()
        if resp == 'Sim'.lower():
            contar = 1
        else: 
            contar = 0
            print("Obrigado por utilizar nosso sistema.")
    except Exception as e:
            print("Está tetando me fazer apresentar problema? Digite somente a Matricula Por favor.")
            contar = 1
        #print(df.isnull().sum())



