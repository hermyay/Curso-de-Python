# Lugares favoritos: Crie um dicionario chamado favorite_places. Pense em tres nomes para usar como chaves do dicionario e armazene de um a tres lugares favoritos para cada pessoa. Para deixar este exercicio um pouco mais interresante, peca a alguns amigos que nomeiem alguns de seus lugares favoritos. Percorra o dicionario com um laco e apresente o nome de cada pessoa e seus lugares favoritos.

favorite_places = {
    'edgar': ['vila das mangas', 'ponta de ouro', 'macaneta'],
    'augusto': ['gorongoza', 'cabora bassa'],
    'cobica': ['madjakaze']
}

for key, value in favorite_places.items():
    print("=="*10)
    print(f"Name: {key}\nfavorite place: ".title())
    for v in value:
        print(f"\t{v}".title()) 
