# Faca um programa que tenha uma funcao chamada ficha(), que receba dois parametros opcionais: o nome de um jogador e quantos golos ele marcou. O programa devera' ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sido informado corectamente.

def ficha(nome, golos):
    nome = str(input("Nome do Jogador: ").title())
    golos = (input("Numero de Golos: "))
    if nome in "":
        nome = "desconhecido"
    if golos == "":
        golos = 0
    return nome,golos


saida = ficha("nome", "golos")
print("-=-"*15)
print("            FICHA DO JOGADOR")
print("-=-"*15)
print(f"      NOME: {saida[0]} | GOLOS: {saida[1]}")
print("-=-"*15)