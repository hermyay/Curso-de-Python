# Albuns dos usuarios: Comece com o seu proprama do Exercicio 8.7. Escreva um laco while que permita aos usuarios fornecer o nome de um artista e o titulo de um album. Depois que tiver essas informacoes, chame make_album() com as entradas do usuario e apresente o dicionario criado. Lembre-se de incluir um valor de saida no laco while.

def make_album(artist_name, album_title):
    '''describle of a music album'''
    print("=="*20)
    album = print(f"\tArtist Name: {artist_name}\n\tAlbum: {album_title}")
    print("=="*20)
    return album

album = dict()
result = list()
while True:
    album['name'] = str(input("Artist Name: "))
    album['album'] = str(input("Album Title: "))
    make_album(album['name'], album['album'])
    question = str(input("Want to input another? [S/N]: "))
    while question not in "Ss":
        if question in "Nn":
            break
        else:
            question = str(input("Please, only aceptible [S/N] leters.\nWant to input another? [S/N]: "))
    result.append(album)
    if question in 'Nn':
        break

print(result)
print("Thank You")
