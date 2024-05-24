def soma (n1, n2):
    return n1+n2

def subtracao (n1, n2):
    return n1-n2

def multiplicacao (n1, n2):
    return n1 * n2

def divisao (n1, n2):
    return n1/n2

def fatorial (n1):
    fatorial = 1
    for n in range(1, n1+1):
        fatorial = fatorial * n
    return fatorial

operacao = int(input("Selecione a operação (1 SOMA, 2 SUBTRAÇÃO, 3 MULTIPLICAÇÃO, 4 DIVISÃO, 5 FATORIAL): "))
if (operacao == 5):
    n1 = int(input("Digite um valor: "))
else:
    n1 = float(input("Digite um valor: "))
    n2 = float(input("Digite outro valor: "))

if (operacao == 1):
    resultado = soma(n1, n2)
elif (operacao == 2):
    resultado = subtracao(n1,n2)
elif(operacao == 3):
    resultado = multiplicacao(n1,n2)
elif(operacao == 4):
    resultado = divisao(n1,n2)
elif(operacao == 5):
    resultado = fatorial(n1)
else:
    resultado = "ERRO"

print(f"RESULTADO: {resultado}")