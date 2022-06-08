# Albuns dos usuarios: Comece com o seu proprama do Exercicio 8.7. Escreva um laco while que permita aos usuarios fornecer o nome de um artista e o titulo de um album. Depois que tiver essas informacoes, chame make_album() com as entradas do usuario e apresente o dicionario criado. Lembre-se de incluir um valor de saida no laco while.

def make_album(artist_name, album_title):
    '''describle of a music album'''
    print("=="*20)
    album = dict()
    album['artist'] = artist_name
    album['album'] = album_title
    print("=="*20)
    return album


while True:
    artist = str(input("Artist Name: "))
    art_album = str(input("Album Title: "))
    question = str(input("Want to input another? [S/N]: "))
    while question not in "Ss":
        if question in "Nn":
            break
        else:
            question = str(input("Please, only aceptible [S/N] inputs.\nWant to input another? [S/N]: "))
    if question in 'Nn':
        break
result = make_album(artist, art_album)
for key, value in result.items():
    print(f"{key} Name: {value}.".title())
    print("=="*20)
