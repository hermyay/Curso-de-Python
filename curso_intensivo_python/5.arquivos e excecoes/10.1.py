# Aprendendo Python: Abra um arquivo em branco em seu editor de texto e escreva algumas linhas que sintetizem o que voce aprendeu sobre Python ate agora. Comece cada linha com a expressao Em Python podemos... Salve o arquivo como learning_python.txt no mesmo diretorio em que estao seus exercicios deste capitulo. Escreva um programa que leia o arquivo e mostre o que voce escreveu, tres vezes. Exiba o conteudo uma vez lendo o arquivo todo, uma vez percorrendo o objecto arquivo com um laco e outra armazenando as linhas em uma lista e entao trabalhando com ela fora do bloco do with.

# Leitura do Arquivo txt e um Prin simples do mesmo.
with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print("==="*20)
    print(contents)
    print("==="*20)

# Leitura do Arquivo percorendo-o com um laco for e o seu print.
file = 'learning_python.txt'

with open(file) as file_object:
    for line in file_object:
        print("==="*20)
        print(line)
        print("==="*20)

# Armazenando o conteudo do arquivo em uma lista e a sua leitura fora da condicao with.
with open(file) as file_object:
    lines = file_object.readlines()

for line in lines:
    print("==="*20)
    print(line)
    print("==="*20)