Algoritmo "Matrizes soma"
// Disciplina   : [Algoritmos e Programa��o]
// Professor   : Fabr�cio Herpich 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Lu�s Ant�nio Fiabani
// Data atual  : 12/06/2024
Var
// Se��o de Declara��es das vari�veis 

valores : vetor[1..3,1..3] de inteiro
c , l, somalinha, somacoluna, principal , secundaria, soma : inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 


para l de 1 ate 3 faca
     para c de 1 ate 3 faca
          valores[l,c] <- randi(10)
     fimpara
fimpara

para l de 1 ate 3 faca
     para c de 1 ate 3 faca
          escreva(valores[l,c])
     fimpara
     escreval()
fimpara


somalinha <- 0
somacoluna <- 0
principal <- 0
secundaria <- 0
soma <- 0
     para c de 1 ate 3 faca
          somalinha <- somalinha + valores[3,c]
     fimpara

      para l de 1 ate 3 faca
          somacoluna <- somacoluna + valores[l,3]
     fimpara
     
para l de 1 ate 3 faca
     para c de 1 ate 3 faca
          se l = c entao
             principal <- principal + valores[l,c]
          fimse
     fimpara
fimpara

para l de 1 ate 3 faca
     para c de 1 ate 3 faca
             soma  <- soma + valores[l,c]
     fimpara
fimpara

para l de 1 ate 3 faca
     para c de 1 ate 3 faca
          se c = 4-l entao
             secundaria  <- secundaria + valores[l,c]
          fimse
     fimpara
fimpara

escreval(somalinha)
escreval(somacoluna)
escreval(principal)
escreval(secundaria)
escreval(soma)
     


Fimalgoritmo