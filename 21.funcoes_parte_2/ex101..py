# Crie um programa que tenha uma funcao chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleicoes.


def voto(ano):
    '''Condicao de votacao para eleicoes segundo a Lei actual.'''
    from datetime import date
    data = date.today().year
    idade = data - ano
    if idade < 18:
        print(f"Saudacoes!\nVOCE TEM: {idade} ANOS\nSUA CONDICAO E': VOTO NEGADO.")
    elif idade < 65:
        print(f"Saudacoes!\nVOCE TEM: {idade} ANOS\nSUA CONDICAO E': VOTO OBRIGATORIO.")
    else:
        print(f"Saudacoes!\nVOCE TEM: {idade} ANOS\nSUA CONDICAO E': VOTO OPCIONAL.")
    print("-=-"*20)
    
    return idade

#programa principal

voto(1992)

# Guanabara

def votar(ano):
    '''Estado do votante para as eleicoes.'''
    from datetime import date
    actual = date.today().year
    idade = actual - ano
    if idade < 16:
        return f"Com {idade} anos: NAO VOTA."
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL."
    else:
        return f"Com {idade} anos: VOTO OBRIGATORIO."

#Programa principal
print(votar(1992))
