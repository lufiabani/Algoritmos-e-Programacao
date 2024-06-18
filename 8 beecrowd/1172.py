X = []
for i in range (0, 10, 1):
    X.append(int(input()))
    if (X[i] == 0 or X[i] < 0):
        X[i] = 1

for i, valor in enumerate(X):
    print(f"X[{i}] = {valor}")