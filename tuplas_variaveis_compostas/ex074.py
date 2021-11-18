# Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla.
# Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estao na tupla.
from random import randint

# Formato 1 de resolucao.
print("=-="*20)
aleat = randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9)
print(f"Os numeros sorteados sao: {aleat}")
print(f"O maior valor e': {max(aleat)}")
print(f"O menor valor e': {min(aleat)}")
print("=-="*20)

# Formato 2 de resolucao.
print("Os numeros sorteados sao: ", end="")
for n in aleat:
    print(f"{n}", end=" ")
print(f"\nO maior valor e': {max(aleat)}")
print(f"O menor valor e': {min(aleat)}")
print("=-="*20)
