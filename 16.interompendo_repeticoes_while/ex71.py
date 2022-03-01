# Crie um programa que simule o funcionamento de um caixa electronico. No inicio pergunte ao usuario qual sera' o valor a ser sacado (numero inteiro) e o programa vai informar quantas cedulas de cada valor serao entregues.
# OBS: Considere que o caixa possui cedulas de MZN50, MZN20, MZN10 e MZN1.

from random import randint
while True:
    pergunta = int(input("Qual e' o valor a ser levantado: "))
    cedula1 = 1
    cedula2 = 10
    cedula3 = 20
    cedula4 = 50
    totalcedulas = cedula1 + cedula2 + cedula3 +cedula4
    while totalcedulas == pergunta:
        randint(totalcedulas)
        print 
    

