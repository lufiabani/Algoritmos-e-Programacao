Algoritmo "Matrizes bidimencionais"
// Disciplina   : [Algoritmos e Programação]
// Professor   : Fabrício Herpich 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 12/06/2024
Var
// Seção de Declarações das variáveis 
mat : vetor[1..3,1..3] de inteiro
l , c :inteiro

ex : vetor[1..3,1..2] de inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

mat[1,2] <- 6

para l de 1 ate 3 faca
     para c de 1 ate 3 faca
          mat[l,c] <- randi(10)
     fimpara
fimpara

para l de 1 ate 3 faca
     para c de 1 ate 3 faca
          escreva (mat[l,c])
     fimpara
     escreval()
fimpara

escreval("---------------------------")

ex[1,1] <- 0
ex[1,2] <- -2
ex[2,1] <- 3
ex[2,2] <- 7
ex[3,1] <- 4
ex[3,2] <- 0

para l de 1 ate 3 faca
     para c de 1 ate 2 faca
          escreva (ex[l,c])
     fimpara
     escreval()
fimpara

Fimalgoritmo