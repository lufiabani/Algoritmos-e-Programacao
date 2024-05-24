#ler arquivos

file = 'exemplo.txt'

teste = open(file , 'r')

print(teste.read())

for indice, linha in enumerate(teste):
    print(indice, linha)

teste.close
