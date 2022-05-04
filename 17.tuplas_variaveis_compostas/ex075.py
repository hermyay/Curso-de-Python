# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) Quantas vezes apareceu o valor 9.
# b) Em que posiço foi digitado o primeiro valor 3.
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
    print(f"O primeiro numero 3 foi digitado em que posicao?: {valor.index(3)+1}ª")
else:
    print("NAO EXISTE NUMERO 3 NESTE CONJUNTO.")
print("=-="*20)
print("Os valores pares sao: ",end="")
if val1 % 2 == 0: print(val1,end=", ")
elif val2 % 2 == 0: print(val2,end=", ")
elif val3 % 2 == 0: print(val3,end=", ")
elif val4 % 2 == 0: print(val4)
else: print("Nao ha valores pares.") # Este metodo nao e' 100% eficaz.

# OUTRA FORMA DE RESOLUCAO DO EXERCICIO

print("=-="*20)
valor2 = tuple(int(input("Digite um numero: "))for v in range(0,4))
print("=-="*20)
print(f"O numero 9 aparece quantas vezes?: {valor2.count(9)}" if 9 in valor2 else "O numero 9 aparece quantas vezes?: NENHUMA.")
print("=-="*20)
print(f"O primeiro numero 3 foi digitado em que posicao?: {valor2.index(3)+1}ª" if 3 in valor2 else "NAO EXISTE O NUMERO 3 NESTE CONJUNTO.")
print("=-="*20)
print("Os valores pares sao: ",end=" ")
print(n for n in valor2 if n % 2 == 0)
print("=-="*20)

# OUTRA MANEIRA DE RESOLVER O EXERCICIO
print("=-="*20)
valores3 = (int(input("Digite o primeiro valor: ")),int(input("Digite o segundo valor: ")),int(input("Digite o terceiro valor: ")),int(input("Digite o quarto valor: "))) # Lembrar que, nas ultimas versoes do python as tuplas dispensam parenteses.
print("=-="*20)
print(f"Voce digitou os seguintes valores: {valores3}")
print("=-="*20)
print(f"O nove aparece {valores3.count(9)} vezes")
print("=-="*20)
if 3 in valores3:
    print(f"O numero 3 foi digitado na {valores3.index(3)+1}ª posicao.")
else:
    print("O valor 3 nao foi digitado em nenhuma posicao.")
print("=-="*20)
print("Os valores pares digitados foram", end=" ")
for n in valores3:
    if n % 2 == 0:
        print(n, end=" ")
