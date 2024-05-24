num = int(input("Digite um número: "))
res = num
while (num != 1):
    res = res * (num-1)
    num = num-1
    print (res, num)

print(res)