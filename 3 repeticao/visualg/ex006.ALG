Algoritmo "semnome"
// Disciplina   : [Algoritmos e Programa��o]
// Professor   : Fabr�cio Herpich 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/04/2024
Var
// Se��o de Declara��es das vari�veis 
i , n , soma : inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

enquanto (i <> 5) faca
escreval("Digite um n�mero: ")
leia (n)
soma <- soma + n
i <- i +1
fimenquanto

escreval (soma)

se (soma % 2 = 0) entao
escreval ("PAR")
senao
escreval ("IMPAR")
fimse
Fimalgoritmo