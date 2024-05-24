def soma(n1,n2):
    return n1+n2

def subtracao(n1,n2):
    return n1-n2

def multiplicacao(n1,n2):
    return n1*n2

def dividir(n1,n2):
    return n1/n2

def menu ():
    print("OPÇÕES: 1 - SOMAR | 2 - SUBTRAIR | 3 - MULTIPLICAR | 4 - DIVIDIR")
    operacao = int(input("Escolha a operação: "))
    if (operacao == 1):
        print(soma(n1,n2))
    elif(operacao == 2):
        print(subtracao(n1,n2))
    elif(operacao == 3):
        print(multiplicacao(n1,n2))
    elif(operacao  == 4):
        print(dividir(n1,n2))
    else:
        print("ERRO DE OPERAÇÃO")

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
menu()