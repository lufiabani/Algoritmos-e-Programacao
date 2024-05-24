sexo = input("Digite o sexo (M or F): ")


n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1+n2+n3+n4)/4

if (media >= 6):
    resultado = "APROVADO"
else:
    resultado = "REPROVADO"
    
if (sexo == "M"):
    print ("Caro aluno, seu resultado é: ", resultado)
else:
    if(sexo == "F"):
        print ("Cara aluna, seu resultado é: ", resultado)
    else:
        print ("ERRO")
