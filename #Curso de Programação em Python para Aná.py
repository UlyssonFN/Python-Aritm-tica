#Curso de Programação em Python para Análise de Dados. 
import datetime as dt
import time as tm

teste = "ola teste"
df = teste[0:3]

print(df)

print(len(teste))
#Indica se o começo da string começa com a palavra que está dentro do parêntese.
print(teste.startswith("Ola"))
#Indica se o começo da string finaliza com a palavra que está dentro do parêntese.
print(teste.endswith("Ola"))
#Conta quantos valores contém dentro da string com base no que está em parêntese.
print(teste.count("e"))
#Deixa o começo da string maiúscula.
print(teste.capitalize())
#verifica se é número 
print(teste.isdigit())
#Deixa tudo maiúsculo
print(teste.upper())
#Deixa tudo minusculo
print(teste.lower())
#Procura onde está a posição do que está escrito dentro do parêntese, senão conter o dado aparecerá -1
print(teste.find("u"))
#Retira os espaços errados da string
print(teste.strip())
#Quebra o texto de acordo com a condição de dentro do parêntese.
print(teste.split(" "))


# Operadores de comparação
# == igual a
# != Diferente
# > Maior que
# < Menor que
# >= Maior ou igual
# <= Menor ou igual

#Indica o que esta (in) ou não esta (not in) em determinada variável
print("ola" not in teste)



#condicionais if e else
#idade = 18
#pessoa = int(input("Digite sua idade :"))

#if pessoa >= idade:
    #print("actived acess")
#elif pessoa >= 15 and pessoa <= 17:
    #print("Father autorized")
#else:
    #print("negative acess")

#Manipulando listas
#Criando uma lista
Lista_Vazia = []
print(Lista_Vazia)
#Adcionandoo valores a lista
Lista_Vazia.append(1)
Lista_Vazia.append(2)
Lista_Vazia.append(3)
Lista_Vazia.append('Valor')
Lista_Vazia.append(1)
print(Lista_Vazia)
#Contando o número de indivíduos na lista
print(len(Lista_Vazia))
#Acessando o valor da lista na posição 0 (sempre inicia em 0)
print(Lista_Vazia[0])
#Acessa o range de 0 até 2
print(Lista_Vazia[0:2])
#Limpar a lista
#Lista_Vazia.clear()
#print(Lista_Vazia)

#Insere o valor de acordo com a posição, porém vai empurrando os outros valores para a direita. 
Lista_Vazia.insert(0, 'teste')
print(Lista_Vazia)

#criação de mais listas
Lista_01 = [0, 1]
Lista_02 = [2, 3]
#Acrescentei a lista 2 dentro da lista 1
Lista_01.extend(Lista_02)
print(Lista_01)

#Remove o valor expecifico na lista, se a lista não conter esse valor apresentará erro.
Lista_01.remove(2)
print(Lista_01)
#remove o valor pelo index, no exemplo foi o index inicial 0, cujo o número 0 era representado por ele. 
Lista_01.pop(0)
print(Lista_01)

Lista_ABC = ['z', 'c', 'f', 'H', 'A']
#Ordena a lista
Lista_ABC.sort()
print(Lista_ABC)
#Inverte a ordem
Lista_ABC.sort(reverse=True)
print(Lista_ABC)
#copia a lista
Lista_nova = Lista_ABC.copy()
print(Lista_nova, Lista_ABC)
#detecta o index do valor na lista
print(Lista_nova.index('H'))

#trás data e hora
Dia_Hoje = dt.datetime.today()
print(Dia_Hoje)
#trás somente data
Dia_Hoje = dt.datetime.today().date()
print(Dia_Hoje)

#Distrincha a data
Ano = Dia_Hoje.year
Mes = Dia_Hoje.month
Dia = Dia_Hoje.day
print(Ano, Mes, Dia)

#cria uma data antiga para armazenamento
Data_Antiga = dt.date(2002, 1, 1)
print(Data_Antiga)
#altera o formato da data para parâmetro br uso atual
DAformato = Data_Antiga.strftime("%d/%m/%y")
print(DAformato)

#soma de datas manual
Soma = Data_Antiga + dt.timedelta(days=30)
print(Soma)
#tempo de 1 segundo para continuar o código
tm.sleep(1)
print("terminar código")
#trás todas as informações de data e hora em tempo real
Agora = tm.localtime()
print(Agora)
#Organiza e formata de acordo com o nosso padrão
AG = tm.strftime('%d/%m/%y, %H:%M:%S', Agora)
print(AG)

