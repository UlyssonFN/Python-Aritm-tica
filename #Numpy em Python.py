#Numpy em Python
import numpy as np

d = [1,2,3,4,5,6]
arr = np.array(d)
#Printa o formato do valor
print(arr.dtype)
#Printa a quantidade de valores de colunas
print(np.shape(arr))
#Printa o tamanho
print(np.size(arr))


d2 = [ [1,3,5,7], [3,55,6,90]]
arr1 = np.array(d2)
#printa na linha 1 o 3 resultado, porque a contagem começa com 0, 1 e 2.
print(arr1[1,2])

#Cria matriz aleatória inteira
print(np.random.randint(0,57, size=(3,3)))

#mútiplicação de Array
arr2 = arr1 * 2
#soma acumulada em numpy
arr2.cumsum(axis=1)
print(arr2)
#cria um novo array
arr4 = np.arange(8)
#Tranforma linha em coluna. 
arr5 = arr4.reshape(4,2)
#Tranforma linha em coluna. 
arr6 = arr5.T
#Concatenar os arrays especificados
arr8 = np.concatenate((arr1, arr2))
print(arr8)

