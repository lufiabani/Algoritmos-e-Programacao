def dmaior (n1, n2, n3):
    aux = n1
    if (n2 > aux):
        aux = n2
    if (n3 > aux):
        aux = n3
    return aux

def dmenor (n1, n2, n3):
    aux = n1
    if (n2 < aux):
        aux = n2
    if (n3 < aux):
        aux = n3
    return aux


n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

print(dmaior(n1,n2,n3))
print(dmenor(n1,n2,n3))