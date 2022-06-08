# Magicos: Crie uma lista de nomes de magicos. Passe a lista para uma funcao chamada show_magicians() que exiba o nome de cada magico da lista.

def show_magicians(magicias):
    '''show the magicians names'''
    c = 0
    for m in magicias:
        c+= 1
        print(f"\tThe {c}ª magician is: {m.upper()}.")

# Programa Principal
magic = list()
for c in range(0,4):
    magic_names = input("Magic name: ")
    magic.append(magic_names)
print("=="*20)
show_magicians(magic)
print("=="*20)