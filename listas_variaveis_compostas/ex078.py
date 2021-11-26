# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

print("=-="*10)
print(f"{'O JOGO DO MAIOR E MENOR':^31}")
print("=-="*10)
valores = list()
for c in range(1, 6):
    valores.append(int(input("Digite um número: ")))
print("=-="*10)
print(f"Digitou os seguintes valores: {valores}")
maior = max(valores)
menor = min(valores)
print("=-="*10)
print(f"O MAIOR valor digitado foi {max(valores)} e se encontra na {valores.index(maior)+1}ª posição.\nO MENOR valor digitado foi {min(valores)} e se encontra na {valores.index(menor)+1}ª posição.")
print("=-="*10)