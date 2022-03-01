'''
                    Variaveis Compostas
As tuplas fazem parte do grupo de variaveis compostas. Ate' este momento estivemos a apreder sobre variaveis simples, `as quais sao atribuidas somente um valor. Nas variaveis compostas ha' a atribuicao de dois ou mais valores.
                            Tuplas
Tupla: E' uma variavel que armazena varios valores. Ou seja, Tupla e' uma variavel composta.

Os elementos da tupla, ou seja, os valores, sao identificados por indices numericos que iniciam, como nas listas, de 0 e os elementos das tuplas sao acessados atraves desses indices numericos.

Se, por exemplo, numa Tupla de variavel "lanche" e com valores "amburguer, sumo, piza, pudim", se quiser mostrar o terceiro valor dessa Tupla, o comando a ser digitado sera: print(lanche[2]) e o valor da saida sera' piza.

Se, por exemplo, na Tupla de variavel "lanche", quiser mostrar na saida os valores "amburguer" e "sumo". O comando a ser executado sera' print(lanche[0,2]).
NB: Note-se que, o ultimo valor "piza" que coresponde ao indice [2] e' sempre ignorado.
NB: As Tuplas sao imutaveis. Uma vez defenida dentro do programa ela se torna imutavel.

Curiosidade: Existem tres tipos de variaveis compostas. As primeiras sao as tuplas, as segundas sao as listas e as terceiras sao os dicionarios.
'''
# Exemplo de uma tupla:
lanche = ("hamburguer","suco","piza","pudim")

# Saida do valor piza:
print(lanche [2])

# Saida dos valores hamburguer e suco:
print(lanche [0:2])

# Saida dos valores suco ate' ao ultimo:
print(lanche [1:])

# Saida ate' o elemento 2:
print(lanche [:2])

# Saida do ultimo valor:
print(lanche [-1])

# Funcao len(). len() significa comprimento e essa funcao serve para dizer quantos elementos tem a tupla, ou seja, quantos valores.
print(len(lanche))

# Usando a estrutura de repeticao for:
for c in lanche:
    print (c)

# As novas versoes do Python aceitam a criacao de Tuplas sem o uso de parenteses:
carros = "mazda", "bmw", "toyota", "kia"
print(carros)

# Teste com uso da estrutura de repeticao for:
for comida in lanche:
    print(f"Eu vou comer {comida}.")
print("Estou cheio!!!")

# Teste com uso da estrutura de repeticao for usando enumerate:
for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posicao {pos}.")
print("Comi muiiito!")

# Teste com uso da estrutura de repeticao for usando len:
for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posicao {cont}")
print("Comi muito!!!")

# Colocando em ordem alfabetica usando a expressao sorted:
print(sorted(lanche))

# Juntando tuplas:
a = 1, 4, 6
b = 2, 3, 4, 8
c = a + b #NB: a + b nao e' o mesmo que b + a em termos de organizacao dos valores.
print(c)

# Usando o metodo cont para contar um elemento:
print(f"O 4 aparece {c.count(4)} vezes.")

# Para mostrar a posicao em que se encontra o elemento:
print(f"O numero 8 esta' na posicao {c.index(8)}")

# Indicando a posicao para comecar a verificacao de posicao, exemplo, iniciando na posicao 2:
print(f"O numero 4 esta' na posicao {c.index(4, 2)}")

# Tupla mista, ou seja, str e numeros:
pessoa = "herminio", 29, "M", 91.72
print(pessoa)

# Apagar a Tupla usando o metodo del. NB: Este metodo serve para apagar qualquer variavel.
del(pessoa)
print(pessoa)
