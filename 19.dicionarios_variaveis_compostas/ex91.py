# Crie um programa em que 4 jogadores jogam um dado e tenham resultados aleatorios. Guarde esses resultados em um dicionario. No final, coloque esse dicionario em orde, sabendo que o vencedor tirou o maior numero no dado.
from msilib import sequence
from operator import itemgetter
from random import randint
from time import sleep
print("Valores lancados:")
sleep(2)
jogadores = {'jogador 1': randint(1,6), 'jogador 2': randint(1,6), 'jogador 3': randint(1,6), 'jogador 4': randint(1,6)}
ranking = dict()
for k, v in jogadores.items():
    print(f"{k} tirou {v} no dado.")
    sleep(2)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print("Ranking dos jogadores:")

for p, r in enumerate(ranking):
    print(f"Em {p}º lugar: {r[0]} com {r[1]}")
    sleep(2)