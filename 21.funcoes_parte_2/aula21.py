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
somar(8, 4) # Neste caso, fica uma lacuna, a nao ser que use o conceito de parametro opcional

# Com parametro opcional
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f"A soma e' igual a {s}") # Podemos colocar o '=0' somente no c, como ultimo valor, mas colocando tambem no 'a' e 'b' faz com que a saida somar possa tambem nao receber nenhum valor alem de so receber dois valores:
    somar(8, 4)
    somar()

#   ESCOPO DE VARIAVEIS

# Em outras palavras, escopo de variaveis, quer dizer, onde a variavel vai funcionar e onde nao vai funcionar. As variaveis globais funcionam tambem no ambiente local, mas as variaveis locais nao funcionam no ambiente global:
def funcao(b):
    n1 = 4
    b += 4
    print(f"N1 dentro e' igual a {n1}") # Este e' o n1 local
    print(f"b dentro igual a {b}") # B e' local

n1 = 2
print(f"N1 fora e' igual a {n1}") # Este e' o n1 global
# print(f"B e' igual a {b}") # Esta declaracao da' erro, pois B e' local e nao pode ser declarado fora.

# No entanto, a formas de levar uma variavel local a ter uma condicao global.

# RETORNO DE VALORES
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f"A soma e' {s}")

somar(3, 2, 5)
somar(2, 2)
somar(4)

# Se for a perceber, todas saidas escrever o valor da mesma for ou seja, "A soma e'" E se quiser mostrar da seguinte forma: "As somas sao 10, 4, 6"? Para as somas sem ter de repetir a soma, substitui-se o comando print pelo comando return:
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

resp = somar(3, 2, 5) # O resultado pode ser jogado dentro de uma variavel ou
print(somar(3, 2, 5)) # dentro de um print ou

r1 = somar(3, 2, 5) # a formatacao que eu quiser.
r2 = somar(1, 7)
r3 = somar(4)
print(f"As somas sao {r1}, {r2}, {r3}.")

# O return e' util quando se quer ter personalizacao de resultados.