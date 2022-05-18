# Animais de estimacao: Crie varios dicionarios, em que o nome de cada dicionario seja o nome de um animal de estimacao. Em cada dicionario, inclua o tipo do animal e o nome do dono. Armazene esses dicionarios em uma lista chamada pets. Em seguida, percorra sua lista com um laco e, `a medida que fizer isso, apresente tudo que voce sabe sobre cada animal de estimacao.

rex = {
    'a_type': 'dog',
    'owner': 'edgar'
}
gertrudes = {
    'a_type': 'cat',
    'owner': 'marcia'
}
mr_slow = {
    'a_type': 'lizart',
    'owner': 'cobica'
}
serpent = {
    'a_type':'snake',
    'owner': 'augusto'
}

pets = [rex, gertrudes, mr_slow, serpent]

for value in pets:
    print("="*10)
    print(f"Animal type: {value['a_type']}\nAnimal owner: {value['owner']}.".title())
    print("="*10)