# Crie um programa que leia o nome e o preco de varios produtos. O programa devera' perguntar se o usuario vai continuar. No final mostre:
# a) Qual e' o total gasto na compra.
# b) Quantos produtos custam mais de MZN1000.
# c) Qual e' o nome do producto mais barato.
maisde1000 = 0
total = 0
menor = 0
contador = 0
barato = " "
while True:
    print("="*40)
    print("         CAIXA DE SUPER MERCADO")
    print("="*40)
    # SECCAO INTRODUCAO DE DADOS
    nome = str(input("Nome do producto: ")).strip().title()
    preco = float(input("Preco do producto MZN: "))

    # SECCAO CONTAR OS DADOS
    contador += 1
    total += preco

    # SECCAO TESTE DE LOGICA
    if preco > 1000:
        maisde1000 += 1
    if contador == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
    print("="*40)
    # SECCAO PERGUNTA
    pergunta = " "
    while pergunta not in "SN":
        pergunta = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]

    # SECCAO BREAK
    if  pergunta == "N":
        break
print("="*40)
print("            FIM DO PROGRAMA")
print("="*40)
    # SECCAO RESULTADOS
print(f"TOTAL COMPRADO: MZN {total}\nPRODUTOS COM O CUSTO MAIS DE MZN1000: {maisde1000}\nPRODUCTO MAIS BARATO: {barato} DE {menor}")
print("="*40)