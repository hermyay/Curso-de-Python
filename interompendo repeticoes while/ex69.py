# Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa devera' perguntar se o usuario quer ou nao continuar. No final, mostre:
# a) Quantas pessoas tem mais de 18 anos.
# b) Quantos homens foram cadastrados.
# c) Quantas mulheres tem menos de 20 anos.
maisde18 = 0
homens = 0
mulheresmenosde20 = 0
while True:
    print("="*40)
    print("          CADASTRE UMA PESSOA")
    print("="*40)

    # SECCAO IDADE
    idade = int(input("Digite a idade: "))

    # SECCAO SEXO
    sexo = " "
    while sexo not in "MF":
        sexo = input("Digite o sexo [M/F]: ").strip().upper()[0]
        if sexo not in "MF":
            print("Por favor, coloque Masculino ou Feminino.")

    # SECCAO PERGUNTA (QUER CONTINUAR?)
    pergunta = " "
    while pergunta not in "SN":
        pergunta = input("Quer continuar? [S/N]: ").strip().upper()[0]
        if pergunta not in "SN":
            print("Digite Sim ou Nao.")

    # SECCAO CONTACAO DOS DADOS
    if idade > 18:
        maisde18 += 1
    if sexo == "M":
        homens += 1
    elif sexo == "F" and idade < 20:
        mulheresmenosde20 += 1

    # SECCAO BREAK
    if pergunta == "N":
        break

    # SECCAO IXIBICAO DOS DADOS
print("="*40)
print("          FIM DO PROGRAMA")
print("="*40)
print(f"NO TOTAL FORAM CADASTRADAS...\nPESSOAS COM MAIS DE 18 ANOS: {maisde18}\nHOMENS: {homens}\nMULHERES COM MENOS DE 20 ANOS: {mulheresmenosde20}")
print("="*40)
