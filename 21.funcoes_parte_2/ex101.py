# Crie um programa que tenha uma funcao chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleicoes.

def voto(ano,idade,cond):
    '''Calculo sobre permissoes de votacao nas eleicoes do ano 2022'''
    
    ano = int(input("Ano de Nascimento: "))
    idade = 2022-ano
    cond = " "
    if idade < 18:
        cond = "NEGADO"
    elif idade < 65:
        cond = "OBRIGATORIO"
    else:
        cond = "OPCIONAL"
    return cond,idade,ano

print("-=-"*30)
nome = str(input("Nome: "))
saida = voto("ano","idade","cond")
print("-=-"*30)
print(f"Saudacoes, {nome.title()}!\nVoce tem: {saida[1]} anos.\nO seu VOTO e': {saida[0]}")
print("-=-"*30)
print(voto())