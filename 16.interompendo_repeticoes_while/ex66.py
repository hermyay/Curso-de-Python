# Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999, que e' a condicao de parada. no final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsidere o flag).
n = s = cont = 0

while True:
    n = int(input("Digite um numero: "))
    if n == 999:
        break
    cont += 1
    s += n
print("PARABENS!!! Voce digitou 999 a CONDICAO DE PARADA.")
print(f"A soma dos {cont} valores digitados e' igual a {s}.")
print("FIM!")