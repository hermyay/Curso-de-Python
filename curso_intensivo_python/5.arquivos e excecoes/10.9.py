# Gatos e cachorros silenciosos: Modifique o seu bloco except do Exercicio 10.8 para falhar silenciosamente caso um dos arquivos esteja ausente.

def pets(files):
    try:
        with open(files) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        print(contents.rstrip().title())

files = 'cats.txt', 'dogs.txt'
for file in files:
    pets(file)