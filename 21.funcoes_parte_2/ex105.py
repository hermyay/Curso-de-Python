# Faca um prorama que tenha uma funcao notas() que pode receber varias notas de alunos e vai retornar um dicionario com as seguintes informacoes:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A media da turma
# - A situacao (opcional)
# Adicione tambem as docstrings

def notas(*valores,situacao=False):
    """
    -> Funcao para analise das notas e situcao do estudante
    : para valores: as notas dos estudantes (aceita varias notas) | 
    PS: o asterixo no principio da variavel indica a condicao de recebimento de varios valores (*n)
    : para situacao: valor opcional (condicao True se quiser visualizar) para demonstracao da situacao do estudante
    : return: dicionario com todas as informacoes relevantes sobre o estudante (nº de notas; a maior, a menor, a media e a situacao)
    """
    resul = dict()
    resul["total"] = len(valores)
    resul["maior"] = max(valores)
    resul["menor"] = min(valores)
    resul["media"] = sum(valores)/len(valores)
    if situacao:
        if resul["media"] < 10:
            resul["situacao"] = "Ruim"
        elif resul["media"] >= 10 < 14:
            resul["situacao"] = "Boa"
        else:
            resul["situacao"] = "Muito Boa"
    return resul


# Programa principal
saida = notas(13, 15,10,12,situacao=True)
print(saida)
help(notas)