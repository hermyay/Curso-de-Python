# Magicos: Crie uma lista de nomes de magicos. Passe a lista para uma funcao chamada show_magicians() que exiba o nome de cada magico da lista.

def show_magicians(m):
    '''show the magicians names'''
    for c in range(0, 6):
        print(f"The {c+1}ª  magicians name is, {m[c]}")

# Programa Principal
magic = ''
result = list()
for magic in range(0, 6):
    magic = str(input("Magic Name: ").title())
    result.append(magic)
print("=="*20)
show_magicians(result)