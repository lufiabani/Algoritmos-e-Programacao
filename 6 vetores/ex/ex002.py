numeros = []
for i in range (0, 15):
    n = int(input("Digite um número: "))
    numeros.append(n)

menor = numeros[0]
indice = 0
for indi, i in enumerate(numeros):
    if (i < menor):
        menor = i
        indice = indi
    
print (f"Indice: {indice} e Numero: {menor}")