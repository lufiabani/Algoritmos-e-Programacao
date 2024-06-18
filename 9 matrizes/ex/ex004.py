import numpy as matriz

valores = matriz.empty((4, 6), dtype=int)

valores[0] = [2 , 3, 5, 2, 4, 8]
valores[1] = [2 , 3, 5, 2, 4, 8]
valores[2] = [2 , 3, 5, 2, 4, 8]
valores[3] = [2 , 3, 5, 2, 4, 8]

total = 0
for l in range (0,4):
    for c in range(0,6):
        total = total + valores[l,c]

print(total)
