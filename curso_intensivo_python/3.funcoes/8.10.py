# Grandes magicos: Comece com uma copia de seu programa do Exercicio 8.9. Escreva uma funcao chamada make_great() que modifique a lista de magicos acrescentando a expressao o Grande ao nome de cada magico. Chame show_magicians() para ver se a lista foi realmente modificada.

def make_great(m):
    for c in range(0, 6):
        print(f"The {c+1}ª  magicians name is, The Great {m[c]}")
    return m

# Programa principal
magic = ''
magicians = list()
for magic in range(0, 6):
    magic = str(input("Magician name: "))
    magicians.append(magic)
result = magicians[:]

make_great(result)
