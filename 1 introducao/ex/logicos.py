a = True
b = False

x = 10
y = -5

#Qual será o resultado após cada passo?

print("(A)", x < y)
print("(B)", x != y)

resultado = (x - 20)
print("(C)", resultado < y)
print("(D)", a and b)
print("(E)", b and a)
print("(F)", a or b)
print("(G)", not(a))
print("(H)", not(x != y))

resultado = a and (x > 10)
print("(I)", resultado)

resultado = a and (x>2) and not (b)
print ("(J)", resultado)