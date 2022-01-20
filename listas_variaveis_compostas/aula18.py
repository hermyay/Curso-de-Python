# Declaracao de uma lista
dados = list()

# Adicao de dados `a lista
dados.append("Herminio")
dados.append(29)
dados.append("Ijaba")
dados.append(19)
dados.append("Joao")
dados.append(40)

# Print do primeiro elemento
print(dados[0])

# Print do segundo elemento
print(dados[1])

# Declaracao de uma outra lista
pessoas = list()

# Adicao de estruturas com uso de fatiamento "[:]" para originar uma copia da estrutura. 
pessoas.append(dados[:]) #NB: Agora tenho uma lista dentro de outra lista.
print(pessoas)

# Outra forma de declarar a mesma estrutura de listas compostas, ou seja, listas dentro de listas.
pessoas = [["Herminio", 29], ["Ijaba", 19], ["Joao", 40]]
print(pessoas)

# Declaracao de elementos da estrutura da sublista, ou seja, da lista dentro de outra lista.
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])

# Exemplo de uso de listas: Declaracao de nome e idade.
for p in pessoas:
    print(f"{p[0]} tem {p[1]} anos de idade.")
print("-=-"*10)

# Exemplo de uso de listas: Leitura de nome e idade e sua posterior declaracao.
visitantes = list()
info = list()
for c in range (0, 5):
    info.append(str(input("Nome: ")))
    info.append(int(input("Idade: ")))
    visitantes.append(info[:])
    info.clear()
print("-=-"*10)
for p in visitantes:
    print(f"{p[0]} tem {p[1]} anos de idade.")
print("-=-"*10)
totalmaior = totalmenor = 0
for p in visitantes:
    if p[1] >= 21:
        print(f"{p[0]} e' maior de idade")
        totalmaior += 1
    else:
        print(f"{p[0]} e' menor de idade.")
        totalmenor += 1
print(f" Temos um total de {totalmaior} maiores de idade \n e um total de {totalmenor} menores de idade.")