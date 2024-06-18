import numpy as matriz

valores = matriz.empty((4, 4), dtype=int)

for l in range (0,4):
    for c in range(0,4):
        valores[l,c] = int(input("Digite o valor: "))

mult = int(input("Digite o valor para multiplicar: "))

valores = valores * 2

print(valores)