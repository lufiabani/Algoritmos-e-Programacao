import numpy as matriz

valores = matriz.empty((10, 10), dtype=int)

for l in range(0,10):
    for c in range(0,10):
        valores[l,c] = 5

print(valores)

#print(valores)
