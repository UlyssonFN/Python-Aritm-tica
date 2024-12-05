#Expressões Regulares em Python
import re

#Procura o padrão em qualquer parte da String
search = re.search('Antonio', 'Rua Antonio Basilio')
print(search)
#Retorna uma lista com todas as ocorrências do padrão na string
findall = re.findall('div', '<div class=conatiner > <div class=barra>')
print(findall)
#Divide uma string com base no padrão
split = re.split('c','Descomplica')
print(split)
#Subistitua o padrão encontrado por outro texto.
sub = re.sub('uma plataforma', 'a melhor plataforma', 'A descomplica é uma plataforma')
print(sub)
#busca todos os números de 0 a 9 e colocarw dentro de uma lista
p = re.compile(r'[0-9]+')
print(p.findall('12 campos de futebol, 10 bnolas, 25 chuteiras'))
