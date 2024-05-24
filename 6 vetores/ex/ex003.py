vetor1 = []
for i in range (0, 20):
    n = int(input("Digite um número: "))
    vetor1.append(n)

vetor2 = []

for i in vetor1:
    if (i == 0):
        vetor2.append(1)
    else:
        vetor2.append(i)

print (vetor2)