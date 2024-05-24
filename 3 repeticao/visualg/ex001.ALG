Algoritmo "semnome"
// Disciplina   : [Algoritmos e Programação]
// Professor   : Fabrício Herpich 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/04/2024
Var
// Seção de Declarações das variáveis 
n , i, soma : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval ("Digite um número inteiro maior que zero: ")
leia (n)

soma <- 0

para i de n-1 ate 0 passo -1 faca
soma <- soma + i
fimpara

escreval (soma)

Fimalgoritmo