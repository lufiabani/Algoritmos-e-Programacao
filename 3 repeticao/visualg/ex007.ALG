Algoritmo "semnome"
// Disciplina   : [Algoritmos e Programação]
// Professor   : Fabrício Herpich
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/04/2024
Var
// Seção de Declarações das variáveis
contador, divisor, numero : inteiro

Inicio
escreva("Digite um número inteiro positivo: ")
leia(numero)

contador <- 0

para divisor de 2 ate numero - 1 faca
     se numero % divisor = 0 entao
        contador <- contador + 1
     fimse
fimpara

se contador = 0 entao
   escreva("O número ", numero, " é primo.")
senao
     escreva("O número ", numero, " não é primo.")
fimse


Fimalgoritmo