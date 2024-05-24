def soma (a, b):
    soma = a + b
    return soma

n1 = float(input("Digite um numero: "))
n2 = float(input("Digite um numero: "))

resultado = soma(n1,n2)
if (resultado % 2 == 0):
    print("É par!")
else:
    print("É Impar")