# INTERACTIVE HELP
# E' um dicionario que ajuda na compressao dos codicos e como escreve-los
help(print)
print(input.__doc__)


# DOCSTRINGS

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    """
    c = i
    while c <= f:
        print(f"{c}", end="..")
        c += p
    print("FIM")

contador(2, 10, 2)

help(contador)

# PARAMETROS OPCIONAIS

def somar(a, b, c):
    s = a + b + c
    print(f"A soma e' igual a {s}")
    
somar(3, 2, 5)