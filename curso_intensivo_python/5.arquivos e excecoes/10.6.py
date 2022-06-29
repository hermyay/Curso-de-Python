# Adicao: Um problema comum quando pedir entradas numericas ocorre quando as pessoas fornecem texto no lugar de numeros. Ao tentar converter a entrada para um int, voce obtera' um TypeError. Escreva um programa que peca dois numeros ao usuario. Some-os e mostre o resultado. Capture o TypeError caso algum dos valores de entrada nao seja um numero e apresente uma mensagem de erro simpatica. Teste seu programa fornecendo dois numeros e, em seguida, digite um texto no lugar de um numero.
sum = list()

try:
    for c in range(0, 2):
        user = int(input(f"{c+1}º number: "))
        sum.append(user) 
except ValueError:
    print("=="*40)
    print("Sum can't be Validated, onlly aceptible integer numbers.")
    print("=="*40)
else:
    print("=="*40)
    result = sum[0] + sum[1]
    print(f"{sum[0]} + {sum[1]} = {result}")
    print("=="*40)