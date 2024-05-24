frase = 'A Caroline torce para Internacional.'

print(frase)

print("torce" in frase)
# Procura a palavra na string (retorna verdadeiro e falso)

print ("internacional" in frase)
# Código ASCII é diferente

print ("Caroline" not in frase)

print(len(frase))
# Indica a quantidade de caracteres

print(frase.lower())
# frase minúscula

print(frase.upper())
# frase maiúscula

print(dir(str))

print(dir(int))

print(frase.capitalize())

print(frase.split())

lista = frase.split()

print (frase[1])

dados = "Fabrício;Internacional;Alto;Loiro;Chato;Baixo"

pessoa = dados.split(";")

print(pessoa)