import datetime as dt
import time as tm

#repete o código duas vezes
for resposta in range(2):
    Data_Hoje = dt.datetime.today().date()

    print('Teste de Humano, sistema de teste')
    print("------------------------------------------")
    Ano = int(input("Digite o Ano Atual :"))
    Mes = int(input("Digite o Mes Atual :"))
    Dia = int(input("Digite o Dia Atual :"))
    print("------------------------------------------")
    Data_Humano = dt.date(Ano, Mes, Dia)
    tm.sleep(1)
    print('Carregando dados status (1%)')
    tm.sleep(2)
    print('Carregando dados status (50%)')
    tm.sleep(1)
    print('Carregando dados status (76%)')
    tm.sleep(2)
    print('Carregando dados status (100%)')
    tm.sleep(1)
    print("------------------------------------------")
    print("Finalização de análise")
    print("------------------------------------------")
    if Data_Humano == Data_Hoje:
        print("Você é humando.")
    else:
        print("Erro de dados inseridos, não reconhecido comandos inseridos, IA detectada")
        print("------------------------------------------")
