# Os Dicionarios sao a terceira estruturas compostas de Python.

# As tuplas sao identificadas pelos parentes, as tuplas pelos parenteses rectos e os Dicionarios pelos colchetes.

# Exemplo da declaracao de um dicionario:
dados = {'nome': "Pedro",'idade': 25}
#NB: Note que, os indices 0 e 1 estao representados pelo 'nome' e 'idade' e suas respectivas variaveis sao "Pedro" e 25.

# Se quisermos mostrar a variavel "Pedro", declaramos o indice 'nome', da seguinte forma:
print(dados['nome'])

# Se quisermos mostrar a variavel 25, declaramos o indice 'idade', da seguinte forma:
print(dados['idade'])

# Nos Dicionarios, a declaracao append nao funciona, neste caso, para adicionar mais uma variavel 'a estrutura usa-se o seguinte metodo:
dados['sexo'] = "M"
# Nesse caso, a variavel 'sexo' sera' adicionado no ultimo indice, neste caso, indice 3, declarado como indice sexo.

# Para o caso de se querer  apagar uma variavel, basta declarar o seguinte:
del dados['idade']
# Assim, a variavel idade e' deletada.

# Outra exemplo da declaracao de um Dicionario:

filme = {
    'titulo':"Star Wars",
    'ano': 1977,
    'director': "George Lucas"
}
# Star Wars, 1977 e George Lucas sao valores e titulo, ano e director sao chaves, e todo o conjunto de valores e chaves sao itens. Sao declarados da seguinte forma.
# Para valores:
print(filme.values())
# Para chaves:
print(filme.keys())
# Para itens:
print(filme.items())

# Exemplo de uma maneira formatada de mostrar os valores e suas recpectivas chaves dos respectivos itens usando a estrutura de repeticao for:
for k,v in filme.items():
    print(f"O {k} e' {v}")

# Voce pode juntar as tuplas, listas e Dicionarios, como no seguinte exemplo:
locadora = []
filme1 = {
        'titulo': "Star Wars",
        'ano': 1997,
        'director': "George Lucas"
    }
filme2 = {
        'titulo': "Avengers",
        'ano': 2012,
        'director': "Joss Whedon"
    }
filme3 = {
        'titulo': "Matrix",
        'ano': 1999,
        'director': "Wachowski"
    }
locadora.append(filme1)
locadora.append(filme2)
locadora.append(filme3)

print(locadora)

# Mostrar o indice 0 da lista:
print(locadora[0])

# Mostrar o indice e o titulo:
print(locadora[0]['titulo'])

# Mostrar o indice e o ano:
print(locadora[1]['ano'])

# Outro exemplo de interaccao entre listas e dicionarios:
#NB: E' importante notar que, em vez do fatiamentos usado nas listas para criar uma copia declarada, nos dicionarios, usa-se a declaracao copy().
movie = dict()
cinema = list()
for c in range(0, 3):
    movie['titulo'] = str(input("Titulo do filme a registar: "))
    movie['ano'] = int(input("ano do filme a registar: "))
    movie['director'] = str(input("Nome do director do filme a registar: "))
    cinema.append(movie.copy())
print(cinema)

# Continuacao do exemplo acima:
for m in cinema:
    for k, v in m.items():
        print(f"O {k} e' {v}.")
    for k in m.values():
        print(k)