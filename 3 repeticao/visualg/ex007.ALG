Algoritmo "semnome"
// Disciplina   : [Algoritmos e Programa��o]
// Professor   : Fabr�cio Herpich
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/04/2024
Var
// Se��o de Declara��es das vari�veis
contador, divisor, numero : inteiro

Inicio
escreva("Digite um n�mero inteiro positivo: ")
leia(numero)

contador <- 0

para divisor de 2 ate numero - 1 faca
     se numero % divisor = 0 entao
        contador <- contador + 1
     fimse
fimpara

se contador = 0 entao
   escreva("O n�mero ", numero, " � primo.")
senao
     escreva("O n�mero ", numero, " n�o � primo.")
fimse


Fimalgoritmo