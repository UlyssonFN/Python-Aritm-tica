#sistema de ponto
import datetime as dt
import sqlite3

def cad_funcionarios():
        a = 1
        while a == 1:
            matricula = int(input('Digite sua Matricula: '))
            name = str(input('Digite seu nome completo: '))
            print('Cadastro realizado com sucesso')
            call = space()
            print('Deseja realizar um novo lançamento: s/n? ')
            respost = int(input('R: '))
            if respost == 's'.lower:
                while a ==1:
                    if respost == 'n'.lower:
                        while a == 0:
                            return()

def space():
    print('-------------------------------------------')
    return()

print('Bem vindo ao sistema de pontos')
call = space()

print('Escolha as opções abaixo')
print('1 - Cadastro de Funcionários')
print('2 - Registro de Ponto')
print('3 - Sair do programa')

resposta = int(input('R: '))

try:
    if resposta == 1: 
        call = cad_funcionarios()
        print
    else:
        if resposta == 2:
            print('Ainda não sei fazer')
        else:
            if resposta == 3:
                print('Programa desligado')
except ValueError:
    print('Erro inesperado')