num = int(input("Digite um número: "))

def fatorial (num):
    if (num == 0 ):
        return 1
    else:
        return (num * (fatorial(num-1)))
    
print(fatorial(num))