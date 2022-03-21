# Aprimore o Desafio 93 para que ele funcione com varios jogadores, incluindo um sistema de visualizacao de detalhes do aproveitamento de cada jogador.

# ex95
while True:
    aproveitamento = {
        'Nome':str(input("Nome do Jogador: ")).title()
    }
    partidas = int(input("Numero de Partidas Jogadas: "))
    print("*"*40)
    golos = list()
    perg = str(input("Quer continuar [S/N]: "))
    if perg in "nN":
        break
for contador in range(1, partidas+1):
    golos.append(int(input(f"Golos na {contador}ª Partida: ")))
aproveitamento['Golos por partida'] = golos[:]
aproveitamento['Total de golos'] = sum(golos)
print("*"*40)
print(aproveitamento)
print("**"*20)
for c, k in aproveitamento.items():
    print(f"{c} : {k}")
print("**"*20)
print(f"O jogador {aproveitamento['Nome']} fez {partidas} Jogos.")
print("**"*20)
for k, v in enumerate(aproveitamento['Golos por partida']):
    print(f"No {k+1}º jogo fez {v} golo(s).")