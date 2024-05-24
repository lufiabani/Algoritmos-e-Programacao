numeros = []
for i in range (0, 10):
    n = int(input("Digite um número: "))
    numeros.append(n)

positivos = []
for i in numeros:
    if (i > 0):
        positivos.append(i)

print(positivos)