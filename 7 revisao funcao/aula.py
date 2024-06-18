alunos = [
    {'nome': 'Diva', 'notas': [9, 8, 10]},
    {'nome': 'Luis', 'notas': [9, 10, 7]},
    {'nome': 'Ivy', 'notas': [7, 10, 8]},
    {'nome': 'Felipe', 'notas': [9, 10, 9]},
]

def calcular_media(notas):
    totalNotas = 0
    media = 0
    for nota in notas:
        totalNotas += + nota
    media = totalNotas / len(notas)
    return (media)

for aluno in alunos:
    print (f'ALUNO: {aluno['nome']} | MÉDIA: {calcular_media(aluno['notas'])}') 

#######################

def somar (a,b,c):
    total  = a+b+c
    print(total)

somar (1,2,3)

##########################

#packing * - multiplos parâmetros
def somar2(*numeros):
    # empacotando - tupla
    print(type(numeros))


    soma = 0
    for numero in numeros:
        soma += numero
    print(soma)

somar2(10,20,31)

def somar3(numero1, numero2):
    somar = numero1+numero2
    print(f'Total: {somar}')

num = [10 ,5]


def calcular_media2(nota1,nota2,ponto_extra=0, kahoot = 0):
    media = (nota1+nota2)/2 + ponto_extra + kahoot
    if (media > 10):
        media = 10
    
    print (media)

calcular_media2(9,8, kahoot = 5)

#funcao anonima / expressao lambda

subtrair = lambda a , b : a - b

print(subtrair(2,2))