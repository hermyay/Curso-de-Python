# As funcoes nas linguagens de programacao, estao vinculadas a palavra ROTINA, ou seja, algo que voce faca constantemente. Nos programas anteriores, usamos funcoes, como por exemplo, na declaracao do print(), input(), len(), int(), float() entre outros, todos estes constituem uma funcionalidade, ou seja, elas sao funcoes, no entanto, estas sao funcoes que ja existem, voce nao necessita declarar o que deve acontecer ou quando deve acontecer.

# Imaginemos uma rotina, em nosso programa, algo que a gente faca varias vezes, constantemente em nosso programa, seria embaracoso ter de escrever o mesmo codigo varias vezes sempre que necessitassemos que executasse aquela funcao.

# Imaginemos que eu necessite, de vez em vez, mostrar uma linha na tela. Posso criar uma funcao para essa especifica funcionalidade, ou seja, mostrar uma linha.


# Para declarar uma funcao personalizada em Python, usamos a declaracao def() que significa, Definicao de Funcao. O objectivo e' criar uma funcao que nao exista no python, ou seja, uma funcao personalizada.

# Ex1 - Funcao mostrar linha:

# Declaracao da Funcao
def mostrarlinha():
    print("-"*21)
# Programa Principal
mostrarlinha()
print("    CURSO EM VIDEO    ")
mostrarlinha()
print("    APRENDA PYTHON    ")
mostrarlinha()
print("    HERMINIO ALVES    ")
mostrarlinha()

#--------------------------------
print("*"*30)
#--------------------------------

#Ex2 - Usando Parametros:

# Declaracao da Funcao
def titulo(txt):
    print("-"*21)
    print(txt)
    print("-"*21)
#Programa Principal
titulo("    CURSO EM VIDEO    ")
titulo("    PYTHON E' MUITO BOM    ")
titulo("    HERMINIO ALVES    ")

#Ex3 - Somatorio de Dois Numeros:
# Declaracao da Funcao
def soma(a, b):
    s = a + b
    print(f"A soma de A = {a} e B = {b}")
    print(f"A soma de A + B = {s}")

# Programa Principal
soma(4, 5)
soma(8, 9)
soma(2, 1)

#Outra Forma
soma(a=4, b=5)
soma(a=9, b=8)
soma(b=2, a=1)

#Ex3 - Empacotamento de Parametros
# Empacotamento de parametros e' uma funcionalidade especial do python. atraves do def exemplo(* parametro) nos declaramos o parametro:
def contador(* num):
    print(num)
    
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# Fora da Tupla
def contador(*num):
    for valor in num:
        print(f"{valor}", end=" ")
    print("FIM")

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# Numero de elementos
def contador(*num):
    tam = len(num)
    print(f"Recebi os valores {num} e sao ao todo {tam} numeros")

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

#Ex4 - Funcoes em Listas
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)