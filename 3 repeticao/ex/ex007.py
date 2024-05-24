numero = int(input("Digite um número positivo: "))

primo = True

for divisor in range(2, numero-1, +1):
    if (numero%divisor == 0):
        primo = False
        


if (primo):
    print("PRIMO")
else:
    print("NÃO PRIMO")