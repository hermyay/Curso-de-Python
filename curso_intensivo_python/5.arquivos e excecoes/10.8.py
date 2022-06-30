# Gatos e cachorros: Crie dois arquivos, cats.txt e dogs.txt. Armazene pelo menos tres nomes de gatos no primeiro arquivo e tres nomes de cachorro no segundo arquivo. Escreva um programa que tente ler esses arquivos e mostre o conteudo do arquivo na tela. Coloque seu codigo em um bloco try-except para capturar o erro FileNotFound e apresente uma mensagem simpatica caso o arquivo nao esteja presente. Mova um dos arquivos para um local diferente de seu sistema e garanta que o codigo no bloco except seja executado de forma apropriada.


def pets(files):
    try:
        with open(files) as f_obj:
            contents = f_obj.read()
            #return contents
    except FileNotFoundError:
        print(f"Sorry, the file {files} was not found.")
    else:
        print(contents.title())
        
    
        
files = 'cats.txt', 'dogs.txt'
for file in files:
    pets(file)