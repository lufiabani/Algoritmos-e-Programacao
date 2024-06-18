import numpy as matriz

valores = matriz.full((4, 3), '', dtype='<U50')

for l in range(0,4):
    for c in range(0,3):
        valores[l,c] = input("Digite as informações: ")

print(valores)