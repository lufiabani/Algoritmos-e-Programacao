nome = input("Digite o nome do aluno: ")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1+n2+n3)/3

print("O ALUNO ", nome, " FOI:")

if (media >= 7 ):
    print ("APROVADO")
else:
    if (media <= 5):
        print ("REPROVADO")
    else:
        print ("EM RECUPERAÇÃO")