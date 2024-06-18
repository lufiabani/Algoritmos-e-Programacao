Algoritmo "semnome"
// Disciplina   : [Algoritmos e Programação (TIC 24.1)]
// Professor   : Fabrício Herpich 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 17/06/2024
Var
// Seção de Declarações das variáveis 
valores : vetor[1..4,1..4] de inteiro
l , c, mult : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

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