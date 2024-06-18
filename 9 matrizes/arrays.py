import numpy as matriz

# criar uma lista simples

lista_do_cassio = [1,2,3,4,5,6,7,8,9]

# criar um array com numpy

meu_array = matriz.array([0,1,2,3,4,5,6])

print(type(lista_do_cassio))
print(type(meu_array))

#operações

print(meu_array + 1)

print(lista_do_cassio + lista_do_cassio)

print(meu_array + meu_array)

print(lista_do_cassio * 2)

meu_array = matriz.array([0,1,2,3,4,5])

print(meu_array * 2)

lista = [1,2,3,4,5,6,7,8,9]

matriz1 = matriz.array([lista,lista,lista])
print(matriz1)

# cria uma matriz a partir dos arrays

matriz2 = matriz.array([meu_array, meu_array, meu_array])
print(matriz2)

matriz3 = matriz.zeros((3,3))
print(matriz3)

#selecionar um valor da matriz na posição 2,3
print(matriz2[2,3])

# negativo seleciona o ultimo valor
print(matriz2[1, -1])

matriz2[0,0] = 1
print(matriz2)

# input dos dados

num_linhas = int(input("Número de linhas: "))
num_colunas = int(input("Número de colunas: "))

# inicializando a matriz vazia

dados = matriz.empty((num_linhas,num_colunas), dtype=int)

# Preencher a matriz com lista usuario

for l in range(0, num_linhas):
    for c in range(0, num_colunas):
        dados[l,c] = int(input(f"Digite valor [{l}][{c}]: "))

print("Dados inseridos na martriz: ")
print(dados)