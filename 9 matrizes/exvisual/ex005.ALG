Algoritmo "semnome"
// Disciplina   : [Algoritmos e Programa��o (TIC 24.1)]
// Professor   : Fabr�cio Herpich 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 17/06/2024
Var
// Se��o de Declara��es das vari�veis 
valores : vetor[1..4,1..4] de inteiro
l , c, mult : inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

para l de 1 ate 4 faca
     para c de 1 ate 4 faca
           leia(valores[l,c])
     fimpara
fimpara

escreval("Multiplicar por: ")
leia(mult)

para l de 1 ate 4 faca
     para c de 1 ate 4 faca
           valores[l,c] <- valores[l,c]*mult
     fimpara
fimpara


Fimalgoritmo