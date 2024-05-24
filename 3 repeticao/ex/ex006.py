n = 0
total = 0
while (n != 5):
    v = float(input("Digite um número: "))
    total = total + v
    n += 1
print(total)

if(total%2 == 0):
    print("Este número é par")
else:
    print("Este número é ímpar")