# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) Quantas vezes apareceu o valor 9.
# b) Em que posicao foi digitado o primeiro valor 3.
# c) Quais foram os numeros pares.
print("=-="*20)
val1 = int(input("Digite o primeiro valor: "))
val2 = int(input("Digite o segundo valor: "))
val3 = int(input("Digite o terceiro valor: "))
val4 = int(input("Digite o quarto valor: "))
valor = val1, val2, val3, val4
print("=-="*20)
print(f"Voce digitou os valores {valor}")
print("=-="*20)
if 9 in valor:
    print(f"O numero 9 aparece quantas vezes?: {valor.count(9)}")
else:
    print(f"O numero 9 aparece quantas vezes?: NENHUMA VEZ.")
print("=-="*20)
if 3 in valor:
    print(f"O primeiro numero 3 foi digitado em que posicao?: {valor.index(3)}a")
else:
    print("NAO EXISTE NUMERO 3 NESTE CONJUNTO.")
print("=-="*20)
print("Os valores pares sao: ",end="")
if val1 % 2 == 0:
    print(val1,end=", ")
if val2 % 2 == 0:
    print(val2,end=", ")
if val3 % 2 == 0:
    print(val3,end=", ")
if val4 % 2 == 0:
    print(val4)
else:
    print("Nao ha valores pares.")

# OUTRA FORMA DE RESOLUCAO DO EXERCICIO

print("=-="*20)
valor2 = tuple(int(input("Digite um numero: "))for v in range(0,4))
print("=-="*20)
print(f"O numero 9 aparece quantas vezes?: {valor2.count(9)}" if 9 in valor2 else "O numero 9 aparece quantas vezes?: NENHUMA.")
print("=-="*20)
print(f"O primeiro numero 3 foi digitado em que posicao?: {valor2.index(3)}a" if 3 in valor2 else "NAO EXISTE O NUMERO 3 NESTE CONJUNTO.")
print("=-="*20)
print("Os valores pares sao: ",end=" ")
print(n for n in valor2 if n % 2 == 0)
print("=-="*20)
