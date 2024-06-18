Algoritmo "semnome"
// Disciplina   : [Algoritmos e Programação (TIC 24.1)]
// Professor   : Fabrício Herpich 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 17/06/2024
Var
// Seção de Declarações das variáveis 
valores : vetor[1..4, 1..3] de caracter

l, c : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

para l de 1 ate 4 faca
     para c de 1 ate 3 faca
          escreval ("Digite o nome, email, CPF")
          leia (valores[l,c])
     fimpara
fimpara

para l de 1 ate 4 faca
     para c de 1 ate 3 faca
          escreva(valores[l,c])
     fimpara
     escreva()
fimpara



Fimalgoritmo