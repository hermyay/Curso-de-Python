# Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas
# b) A media de idade do grupo
# c) Uma lista com todas as pessoas com idade acima da media.

pessoas = dict()
dados = list()
soma = media = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input("Nome: ").title())

    while True:
        pessoas['sexo'] = str(input("Sexo: [M/F] ").upper()[0])
        if pessoas["sexo"] in "MmFf":
            break
        print("ERROR.")

    pessoas['idade'] = int(input("Idade: "))
    soma += pessoas["idade"]
    dados.append(pessoas.copy())

    while True:
        pergunta = str(input("Quer continuar? [S/N]: ").upper()[0])
        if pergunta in "SsNn":
            break
        print("ERROR.")

    if pergunta == "N":
        break

print(dados)
print("**"*20)

print(f"A) Foram cadastradas {len(dados)} pessoas.")
print("**"*20)

media = soma / len(dados)

print(f"B) A media de idade do grupo e'de {media:.0f} Anos")

print("**"*20)
print("C) A(s) pessoa(s) com idade acima da media: ", end=" ")
for p in dados:
    if p['idade'] > media:
        print(f"{p['nome']}", end=" | ")
print("\n")

print("**"*20)
print("D) As mulheres cadastradas foram: ", end="")
for p in dados:
    if p['sexo'] in "Ff":
        print(f"{p['nome']}", end=" | ")
print("\n")

print("**"*20)
print("E) Os homens cadastrados foram: ", end="")
for p in dados:
    if p['sexo'] in "Mm":
        print(f"{p['nome']}", end=' | ')
print("\n")

print("**"*20)
print("F) Pessoas menores de 18 anos: ", end="")
for p in dados:
    if p['idade'] < 18:
        print(f"{p['nome']}", end=' | ')
print("\n")
print("**"*20)
print("G) Pessoas maiores de 18 anos: ", end="")
for p in dados:
    if p['idade'] > 18:
        print(f"{p['nome']}", end=" | ")
print("\n")
print("**"*20)