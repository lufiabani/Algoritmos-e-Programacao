Algoritmo "semnome"
// Disciplina   : [Algoritmos e Programa��o]
// Professor   : Fabr�cio Herpich
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/04/2024
Var
// Se��o de Declara��es das vari�veis
n1 , n2 : inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc...

escreval ("Digite um n�mero: ")
leia (n1)
escreval ("Digite um n�mero maior: ")
leia (n2)

repita
se (n1%2 <> 0) entao
escreva (n1)
fimse

n1 <- n1 +1

ate (n1 = n2)

Fimalgoritmo