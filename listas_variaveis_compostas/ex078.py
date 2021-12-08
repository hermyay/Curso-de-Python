# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

print("=-="*10)
print(f"{'O JOGO DO MAIOR E MENOR':^31}")
print("=-="*10)

valores = list()
for c in range(0, 5):
    valores.append(int(input(f"Digite um número para a posicao {c}: ")))


print("=-="*10)
print(f"Digitou os seguintes valores: {valores}")

maior = max(valores)
menor = min(valores)

print("=-="*10)
print(f"O MAIOR valor digitado foi {max(valores)} e se encontra nas posiçoes",end=" ")

# Se o valor digitado for igual a maior, ou seja, `a variavel que recebe o maior valor digitado, imprima a posicao desse valor, ou, posicoes desse valor.
for i, v in enumerate(valores):
    if v == maior:
        print(f"{i}...",end=" ")
print()

print(f"O MENOR valor digitado foi {min(valores)} e se encontra nas posiçoes",end=" ")
for i, v in enumerate(valores):
    if v == menor:
        print(f"{i}...",end="")
print()
print("=-="*10)