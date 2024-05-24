# Interpolacao

carro = "Lancer"
ano = 2014
preco = 89999.0

#inteporlação de texto
print("Carro: " + carro + " , Preço: " + str(preco))
# print("Carro: " + carro + " , Preço: " + preco) -> nao concatena tipos de dados diferentes
print("Carro: ", carro , " , Preço: ", preco)

# Formas antigas de interpolação

print("Carro %s, ano %d, preço: %f" % (carro, ano, preco)) #pouco utilizada

#versões mais novas
print("Carro: {0}, ano: {1}, preço: {2}" .format(carro, ano, preco))

#versão atual
print(f'Carro: {carro}, Ano: {ano}, Preço: {preco}')
