Algoritmo "semnome"
// Disciplina   : [Algoritmos e Programa��o]
// Professor   : Fabr�cio Herpich 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/04/2024
Var
// Se��o de Declara��es das vari�veis 
n , i, soma : inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval ("Digite um n�mero inteiro maior que zero: ")
leia (n)

soma <- 0

para i de n-1 ate 0 passo -1 faca
soma <- soma + i
fimpara

escreval (soma)

Fimalgoritmo