# Crie um programa que simule o funcionamento de um caixa electronico. No inicio pergunte ao usuario qual sera' o valor a ser sacado (numero inteiro) e o programa vai informar quantas cedulas de cada valor serao entregues.
# OBS: Considere que o caixa possui cedulas de MZN50, MZN20, MZN10 e MZN1.

import random
while True:
    pergunta = int(input("Qual e' o valor a ser levantado: "))
    random.randint(50,20,10,1)
    print(f"levantou {pergunta} notas")
