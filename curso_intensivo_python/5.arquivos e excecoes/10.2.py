# Aprendendo C: Voce pode usar o metodo replace() para substituir qualquer palavra por uma palavra diferente em uma string. Eis um exemplo rapido que mostra como substituir a palavra 'dog' por 'cat' em uma frase:

message = "I really like dogs."
print(message.replace('dogs', 'cats'))
# Leia cada linha do arquivo learning_python.txt que voce acabou de criar e substitua a palavra Python pelo nome de outra linguagem, por exemplo, C. Mostre cada linha modificada na tela.
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.replace("python", "C").strip())
    