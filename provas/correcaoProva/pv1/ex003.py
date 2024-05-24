a = 2
area = 3.14159 * a ** 2
print('A=%.4f' %area)

"""
Algoritmos "3b"

Var
    a, i : inteiro
Inicio
    a <- 1;
    i <- 0;
    enquanto i<8 faca
        a<- a * 2
        i<- a + 1
    fimenquanto

    escreval(a)
    escreval(i)
Fimalgoritmo


Algoritmo "3c"

Var
    n,p : inteiro
Inicio
    n<- 0;
    p <- 0;
    enquanto n <10 faca
        n<- n+3
        p <- n+1
    fimenquanto

    escreval(n)
    escreval(p)
Fimalgoritmo
"""

x = 3
y = 5
z = 7

if x > 5:
    z -= 1
else:
    if y <100:
        z=0
    else:
        z = 1
if z == 0:
    x = y
else:
    y = x

print(x)
print(y)
print(z)
