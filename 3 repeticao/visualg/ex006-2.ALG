Algoritmo "semnome"
// Disciplina   : [Algoritmos e Programação]
// Professor   : Fabrício Herpich
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/04/2024
Var
// Seção de Declarações das variáveis
i , n , soma : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
para i de 1 ate 5 passo 1 faca
escreval("Digite um número: ")
leia (n)
soma <- soma + n
fimpara

escreval (soma)

se (soma % 2 = 0) entao
escreval ("PAR")
senao
escreval ("IMPAR")
fimse
Fimalgoritmo