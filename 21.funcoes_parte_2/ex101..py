# Crie um programa que tenha uma funcao chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleicoes.


def voto(username = str(input("Nome: "))):
    '''Calculo de estado de votacao para eleicoes 2022'''
    perg = int(input("ANO DE NASCIMENTO: "))
    print("-=-"*30)
    ano = (2022-perg)
    if ano < 18:
        print(f"Saudacoes, {username.title()}!\nVOCE TEM {ano} ANOS.\nSUA CONDICAO E': VOTO NEGADO.")
    elif ano < 65:
        print(f"Saudacoes, {username.title()}!\nVOCE TEM {ano} ANOS.\nSUA CONDICAO E': VOTO OBRIGATORIO.")
    else:
        print(f"Saudacoes, {username.title()}!\nVOCE TEM {ano} ANOS.\nSUA CONDICAO E': VOTO OPCIONAL.")
    print("-=-"*30)

    return perg, username

voto()