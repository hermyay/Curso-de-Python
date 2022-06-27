# Rios: Crie um dicionario que contenha tres rios importantes e o pais que cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'.
# Use um laco para exibir uma frase sobre cada rio, por exemplo, O Nilo corre pelo Egito.
# Use um laco para exibir o nome de cada rio incluido no dicionario.
# Use um laco para exibir o nome de cada pais incluido no dicionario

river = dict()

river['limpopo'] = "Mozambique"
river['zambeze'] = 'Zimbabwe'
river['nilo'] = 'Egipto'

# Frase sobre cada rio
for key,value in river.items():
    print(f"O {key} corre em {value}.")
print("=="*20)

# Nome de cada rio
for name in river.keys():
    print(name)
print("=="*20)

# Nome de cada pais
for name in river.values():
    print(name)
print("=="*20)