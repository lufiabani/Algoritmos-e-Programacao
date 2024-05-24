""" Listas - Arrays ou Vetores

Mutável e dinâmica, Heterogenea e Indexada

"""

lista = ['Segunda Guerra', 'Primeira Guerra', 'Queda do muro de Berlim', 'Achamento do Brasil']

print(type(lista))
print(dir(lista))
print(lista [1]) # Forma de acessar as informações de uma lista (usando colchete) - começa no zero
print(lista [2])
print(lista [-1]) #último item da lista
print(lista[:2]) #acesso aos dois primeiros itens
print(lista[1:4]) # acesso aos itens do intervalo
print(lista[::2]) #pula de dois em dois

lista[0] = "alterado" #Alterou o item da lista (mutavel/dinamica)
print(lista)

lista.append(5) #adiciona um item na lista
print(lista)

lista.remove('Queda do muro de Berlim') #deleta um item da lista pelo texto
print(lista)

del lista[0] #deleta um item da lista pelo indice
print(lista)

print(len(lista)) # quantidade de itens na lista

print(lista.count('Primeira Guerra')) # indica a quantidade de repetições na lista

print(lista.index('Primeira Guerra')) # indica o index do item

lista.reverse() # invertendo uma lista
print(lista)

lista.sort() #ordena de forma alfabética a lista
print(lista)

print('Primeira Guerra' in lista)
print('Primeira Guerra' not in lista)

lista.clear() #limpando a lista
print(lista)
