def soma (num):
    resultado = 0
    for i in range(num, 0, -1):
        resultado = resultado + i
    return (resultado)

num = int(input("Escreva um número positivo: "))

print(soma (num))