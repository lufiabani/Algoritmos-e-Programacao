numero = int(input("Digite um número inteiro: "))

print("Tabuada de multiplicação de", numero, ":")

i = 1

while i <= 10:
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
    i += 1