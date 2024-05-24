def somatorio (numero):
    if (numero <= 0):
        return(0)
    else:
        return(numero + somatorio(numero-1))
    
numero = int(input("Digite um número: "))
print(f"O somatório é: {somatorio(numero)}")