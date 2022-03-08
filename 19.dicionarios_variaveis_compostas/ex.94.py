# Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas
# b) A media de idade do grupo
# c) Uma lista com todas as pessoas com idade acima da media.

pessoas = dict()
dados = list()
soma = media = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input("Nome: "))
    while True:
        pessoas['sexo'] = str(input("Sexo: "))
        if pessoas["sexo"] in "MmFf":
            break
        print("ERROR.")
    pessoas['idade'] = int(input("Idade: "))
    
    dados.append(pessoas.copy())
    while True:
        pergunta = str(input("Quer continuar? [S/N]: "))
        if pergunta in "SsNn":
            break
        print("ERROR.")
    if pergunta == "N":
        break

print(dados)
        #print("Por favor, precione a tecla S para Sim ou N para Nao.")
    #elif pergunta in "Nn":
     #   break    

    #print(f"{len(dados)} pessoa cadastrada.")

print(f"Foram cadastradas {len(dados)} pessoas.")

#soma += pessoas["idade"]
media = soma / len(dados)
print(f"A media de idade do grupo e': {media:5.2f}")
print(soma)
print(dados)
#print(pessoas["idade"])