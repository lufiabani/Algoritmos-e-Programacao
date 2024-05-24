numeros = []
for i in range (0, 6):
    n = int(input("Digite um número: "))
    numeros.append(n)

negativos = 0
listaneg = []
for numero in numeros:
    if (numero < 0):
        listaneg.append(numero)
        negativos += 1

for negativo in listaneg:
    print(negativo)

print(negativos)