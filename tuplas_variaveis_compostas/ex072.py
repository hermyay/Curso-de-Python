# Crie um programa que tenha uma tupla totalmente preechida com uma contagem por extenso, de zero ate' vinte.
# Seu programa devera' ler um numero pelo teclado (entre 0 e 20) e mostra'-lo por extenso.

numero = "zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "desasseis", "dezassete", "dezoito", "dezanove", "vinte"
questao = int(input("Digite um numero entre 0 e 20 e saiba o seu valor em extenso: "))
print(f"Voce digitou o numero {numero[questao]}")
