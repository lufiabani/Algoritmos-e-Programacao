A = []

for i in range (0,10,1):
    A.append(float(input()))

for i, valor in enumerate(A):
    if(valor <= 10):
        print(f"A[{i}] = {valor}")
