#Limite de 170 linhas de leitura
arquivo = 'cidades.txt'

cidades = open(arquivo, 'r')
print(cidades.read())
"""
for indice, cidade in enumerate(cidades):
    print(indice, cidade)

cidades.close()
"""