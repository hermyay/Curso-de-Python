# Glossario: Um dicionario Python pode ser usado para modelar um dicionario de verdade. No entanto, para evitar confusao, vamos chama-lo de glossario.
# Pense em cinco palavras relacionadas `a programacao que voce conheceu nos capitulos anteriores. Use essas palavras como chaves em seu glossario e armazene seus significados como valores.
# Mostre cada palavra e seu significado em uma saida formatada de modo elegante. Voce pode exibir a palavra seguida de dois pontos e depois o seu significado, ou apresentar a palavra em uma linha e entao exibir seu significado indentado em uma segunda linha. Utilize o caractere de quebra de linha para inserir uma linha em branco entre cada par palavra-significado em sua saida.
glossario = dict()
glossario["print"] = "Mostrar algo na tela"
glossario["list"] = "Criar uma lista"
glossario["tuple"] = "Criar uma lista de valores inalteraveis"
glossario["while"] = "Estruta de repeticao"
glossario["while True"] = "Estrutura de repeticao initerupta"
for key,value in glossario.items():
    print(f"{key}: {value}.")