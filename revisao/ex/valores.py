indice = 0

numero = int(input('Digite um numero: '))
maior = numero
menor = numero
while (indice != 10):
    numero = int(input('Digite um numero: '))
    if (numero < menor):
        menor = numero
    elif (numero > maior):
        maior = numero
    indice += 1

print (maior, menor)