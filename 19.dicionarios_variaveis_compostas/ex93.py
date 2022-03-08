# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de golos feitos em cada partida. No final, tudo isso sera' guardado em um dicionario, incluindo o total de golos feitos durante o campeonato.

aproveitamento = {
    'Nome':str(input("Nome do Jogador: ")).title()
}
partidas = int(input("Numero de Partidas Jogadas: "))
print("*"*40)
golos = list()
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