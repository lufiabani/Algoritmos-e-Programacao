Algoritmo "semnome"
// Disciplina   : [Algoritmos e Programação]
// Professor   : Fabrício Herpich 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/04/2024
Var
// Seção de Declarações das variáveis 
n1 , n2 : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

escreval ("Digite um número: ")
leia (n1)
escreval ("Digite um número maior: ")
leia (n2)

repita
se (n1%2 = 0) entao
escreva (n1)
fimse

n1 <- n1 +1

ate (n1 = n2)

Fimalgoritmo