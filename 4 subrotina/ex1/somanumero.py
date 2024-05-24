def soma (num):
    resultado = 0
    while(num != 0):
        resultado = resultado + num
        num = num -1
    return (resultado)

num = int(input("Escreva um número positivo: "))

print(soma (num))