# Lugares em restaurante: Escreva um programa que pergunte ao usuario quantas pessoas estao em seu grupo para jantar. Se a resposta for maior que oito, exiba uma mensagem dizendo que eles deverao esperar uma mesa. Caso contrario, informe que sua mesa esta pronta.

question = int(input("Dear costumer.\nHow many people are with you for dinner? "))

if question > 8:
    print("Please, wait for a table!")
else:
    print("Your table is ready.")