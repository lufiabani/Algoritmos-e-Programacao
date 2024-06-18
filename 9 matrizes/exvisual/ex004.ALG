Algoritmo "semnome"
// Disciplina   : [Algoritmos e Programação (TIC 24.1)]
// Professor   : Fabrício Herpich 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 17/06/2024
Var
// Seção de Declarações das variáveis 
valores : vetor[1..4,1..6] de inteiro
total, l, c : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

para l de 1 ate 4 faca
     para c de 1 ate 6 faca
          valores[l,c] <- randi(4)
     fimpara
fimpara

total <- 0

para l de 1 ate 4 faca
     para c de 1 ate 6 faca
          total <- valores[l,c] + total
     fimpara
fimpara

escreval (total)


Fimalgoritmo