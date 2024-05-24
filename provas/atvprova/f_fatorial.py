#GRUPO: Diva Moreira, Luís Fiabani, Luiz Angelo // função corrigida
def funcao_fatorial(num):
    fatorial = 1
    for i in range(1,num+1):
        fatorial = fatorial*i
    return(fatorial)

num = int(input("Digite um número inteiro: "))
if(num>=0):
    print(f"O fatorial do número {num} é {funcao_fatorial(num)}")
else:
    print(f"Número inválido (menor do que zero)")