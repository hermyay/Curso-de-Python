# Crie um programa que tenha uma funcao chamada voto()
# que vai receber como parametro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto
# NEGADO, OPCIONAL ou OBRIGATORIO nas eleicoes.

def voto(ano = 0,idade = 0,cond = " "):
    '''Calculo sobre permissoes de votacao nas eleicoes do ano 2022'''
    from datetime import date
    actualdate = date.today().year
    idade = actualdate-ano
    if idade < 18:
        cond = "NEGADO"
    elif idade < 65:
        cond = "OBRIGATORIO"
    else:
        cond = "OPCIONAL"
    return cond,idade,ano


# Programa Principal
print("-=-"*20)
nome = str(input("Nome: "))
data = int(input("Ano de nascimento: "))
saida = voto(data)
print("-=-"*20)
print(f"Saudacoes, {nome.title()}!\nVoce tem: {saida[1]} anos.\nO seu VOTO e': {saida[0]}")
print("-=-"*20)
