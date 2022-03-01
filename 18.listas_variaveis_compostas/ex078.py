# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

# Apresentacao do Jogo.
print("=-="*10)
print(f"{'O JOGO DO MAIOR E MENOR':^31}")
print("=-="*10)

# Criacao da Lista a receber valores.
valores = list()
for c in range(0, 5):
    valores.append(int(input(f"Digite um número para a posicao {c}: ")))

# Apresentacao dos valores e criacao de variaveis para o maior e o menor valor.
print("=-="*10)
print(f"Digitou os seguintes valores: {valores}")

maior = max(valores)
menor = min(valores)

# Apresentacao do maior valor digitado.
print("=-="*10)
print(f"O MAIOR valor digitado foi {max(valores)} e se encontra nas posiçoes",end=" ")

# Para apresentacao das posicoes do maior valor digitado, no caso de o mesmo valor ser digitado duas ou mais vezes.
# Se o valor digitado for igual `a variavel maior, ou seja, `a variavel que recebe o maior valor digitado, o programa imprime a posicao desse valor, ou, em caso do valor ser apresentado em duas ou mais posicoes, imprime as posicoes desse valor.
for i, v in enumerate(valores):
    if v == maior:
        print(f"{i}...",end=" ")
print()

# Apresentacao do menor valor digitado.
print(f"O MENOR valor digitado foi {min(valores)} e se encontra nas posiçoes",end=" ")

# Apresentacao das posicoes dos menores valores digitados, seguindo a logica de programacao para o maior valor digitado.
for i, v in enumerate(valores):
    if v == menor:
        print(f"{i}...",end="")
print()
print("=-="*10)