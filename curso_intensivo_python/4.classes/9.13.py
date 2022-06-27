# Reescrevendo o programa com OrderedDict: Comece com o Exercicio 6.4, em que usamos um dicionario-padrao para representar um glossario. Reescreva o programa usando a classe OrderedDict e certifique-se de que a ordem da saida coincida com a ordem em que os pares chave-valor foram adicionados ao dicionario.

# Exercicio 6.4 
# Glossario: Um dicionario Python pode ser usado para modelar um dicionario de verdade. No entanto, para evitar confusao, vamos chama-lo de glossario. Pense em cinco palavras relacionadas `a programacao que voce conheceu nos capitulos anteriores. Use essas palavras como chaves em seu glossario e armazene seus significados como valores. Mostre cada palavra e seu significado em uma saida formatada de modo elegante. Voce pode exibir a palavra seguida de dois pontos e depois o seu significado, ou apresentar a palavra em uma linha e entao exibir seu significado indentado em uma segunda linha. Utilize o caractere de quebra de linha para inserir uma linha em branco entre cada par palavra-significado em sua saida.
from collections import OrderedDict

glossary = OrderedDict()
glossary['print'] = 'mostrar algo na tela'
glossary['fuction'] = 'funcao'
glossary['dict'] = 'dicionario no python'

for key, value in glossary.items():
    print(f"{key}: {value}")
