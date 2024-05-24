n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if (n1>n2):
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

resultado = maior - menor

print(resultado)