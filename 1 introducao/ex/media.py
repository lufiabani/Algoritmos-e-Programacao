nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))

media = (nota1 + nota2)/2

print("A média entre as notas é: ", media)
resultado = (media >= 5.75)

if (resultado):
    print("passou")
else:
    print ("Reprovou")