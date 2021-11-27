# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correcta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

valores =list()
n = int(input("Digite o primeiro numero: "))
valores.append(n)
print(f"O valor {n} esta na ultima posicao.")

n1 = int(input("Digite o segundo numero: "))
valores.append(n1)
if n1 > n:
    print(f"O valor esta na ultima posicao.")
else:
    print(f"O valor esta na primeira posicao.")

n2 = int(input("Digite o terceiro valor: "))
valores.append(n2)
if n2 > n1 > n:
    print(f"O valor esta na ultima posicao")
elif n1 > n2 < n:
    print("O valor esta na segunda posicao.")
elif n2 < n1 < n:
    print("O valor esta na primeira posicao.")
else:
    print("O valor esta na terceira posicao.")

n3 = int(input("Digite o quarto valor: "))
valores.append(n3)
if n3 > n2 > n1 > n:
    print("O valor esta na ultima posicao.")
elif n2 > n3 < n1 < n:
    print("O valor esta na terceira posicao.")
elif n2 > n1 > n3 < n:
    print("O valor esta na segunda posicao.")
elif n3 < n2 < n1 < n:
    print("O valor esta na primeira posicao.")
else:
    print("O valor esta na quarta posicao")

n4 = int(input("Digite o quinto valor: "))
valores.append(n4)
if n4 > n3 > n2 > n1 > n:
    print("O valor esta na ultima posicao.")
elif n3 > n2 > n4 > n1 > n:
    print("O valor esta na terceira posicao.")
elif n3 > n4 > n2 > n1 > n:
    print("O valor esta na quarta posicao.")
elif n3 > n2 > n1 > n4 < n:
    print("O valor esta na segunda posicao.")
else:
    print("O valor esta na primeira posicao.")
print(valores)

'''
n4 = n > n3

n0 = n < n1
print(f"O valor {n0} esta na primeira posicao.")
n2 = n > n0
print(f"O valor {n2} esta na terceira posicao.")
n1 = n < n2
print(f"O valor {n2} esta na segunda posicao.")
n3 = n > n2
print(f"O valor {n3} esta na quarta posicao.")
print(valores)
    
n = int(input("Digite um numero: "))
valores.append(n)
if n[0]:
    n = valores(min)
if n[2]:
    n = n > n[0] < n[4]
if n[1]:
    n = n < n[2]
else:
    n = n[3]
'''
    