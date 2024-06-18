import numpy as matriz

valores = matriz.array([[1 ,2, 3],[4,5,6],[7,8,9]])

print(valores)

for l in range(0 , 3):
    for c in range(0 ,3):
        print(valores[l,c])