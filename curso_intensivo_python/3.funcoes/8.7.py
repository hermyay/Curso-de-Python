# Album: Escreva uma funcao chamada make_album() que construa um dicionario descrevendo um album musical. A funcao deve aceitar o nome de um artista e o titulo de um album e deve devolver um dicionario contendo essas duas informacoes. Use a funcao para criar tres dicionarios que representem albuns diferentes. Apresente cada valor devolvido para mostrar que os dicionarios estao armazenando as infrmacoes do album correctamente.

def make_album(artist_name, album_title):
    '''describle of a music album'''
    album = dict()
    album['artist'] = artist_name
    album['album'] = album_title
    return album

first_album = make_album('Bob Marlem', 'One Love')
print(first_album)
second_album = make_album('ColdPlay', 'Viva La Vida')
print(second_album)
third_album = make_album('Eminem', 'unknown')
print(third_album)
total_albuns = first_album, second_album, third_album

print(total_albuns)
print(total_albuns[0])