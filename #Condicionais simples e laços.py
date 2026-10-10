#Condicionais simples
x = int(input('Enter a number: '))
y = int(input('Enter another number: '))
if x > y:
    print('O primeiro valor é maior que o segundo!')
    
x = int(input('Enter a number: '))
y = int(input('Enter another number: '))
if x > y:
    print('O primeiro valor é maior que o segundo!')
if x < y:
    print('O segundo valor é maior que o primeiro!')

#Condicionais compostas
x = int(input('Enter a number: '))
y = int(input('Enter another number: '))
if x > y:
    print('O primeiro valor é maior que o segundo!')
else:
    print('O segundo valor é maior que o primeiro!')
    
    
#par ou impart
x = int(input('Digite um valor inteiro: '))
if x % 2 == 0:
    print('O valor é par!')
else:
    print('O valor é ímpar!')
    
#contagem for

for i in (1,10,2):
    print(i)