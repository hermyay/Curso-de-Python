# Faca um programa que leia o nome e o peso de varias pessoas, guardando tudo em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas.
# b) Uma listagem com as pessoas mais pesadas.
# c) Uma listagem com as pessoas mais leves.

dados = list()
lista = list()
maior = menor = 0
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    perg = str(input("Para continuar, digite [S]\nPara terminar digite [N]: "))
    if perg in "Nn":
        break
print("-=-"*20)
print(f"Foram cadastradas {len(lista)} pessoas.")
print("-=-"*20)
print(f"O maior peso e' de {maior}Kg e pertence `a",end=" ")
for p in lista:
    if p[1] == maior:
        print(f"{p[0]}.")
print(f"O menor peso e' de {menor}Kg e pertence `a",end=" ")
for p in lista:
    if p[1] == menor:
        print(f"{p[0]}.")
