# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de golos feitos em cada partida. No final, tudo isso sera' guardado em um dicionario, incluindo o total de golos feitos durante o campeonato.

aproveitamento = {
    'nome':str(input("Nome do Jogador: ")),
    'partidas':int(input("Numero de Partidas Jogadas: ")),
}

for p in aproveitamento['partidas']:
    aproveitamento['golos'] = int(input("Quantidade de Golos/Partida: "))