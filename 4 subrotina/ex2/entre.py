def verifica (numero):
    if(numero <= 10 and numero >= 0):
        print('sim')
    else:
        print("nao")

numero = int(input("Digite um número: "))
verifica(numero)