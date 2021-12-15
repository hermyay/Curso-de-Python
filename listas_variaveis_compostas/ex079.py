# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Apresentacao do Programa.
print("=-="*20)
print(f"{'FICHA DE CADASTRO DE NUMEROS SEM REPETICAO DE VALORES':^62}")
print("=-="*20)

# Criacao da Lista de recebimento de cadastros e da declaracao de valores ja adicionados.
valores = []
while True:
    n = int(input("Digite o valor: "))
    if n not in valores:
        valores.append(n)
    else:
        print("O valor já foi adicionado.")
    

# Criacao da pergunta para parar, ou nao, recebimento de novos valores.
    perg = input(str("Quer continuar? [S/N]: ")).strip().upper()[0]

# Direccionamento `as opcoes de reposta `a pergunta sobre recebimento de novos valores.
    while perg not in "SsNn":
        perg = input(str("Por favor, digite Sim ou Nao.\nQuer continuar? [S/N]: ")).strip().upper()[0]

# Paragem para o recebimento de novos valores. Break.
    if perg in "Nn":
        print("=-="*20)
        valores.sort()
        print(f"Os numeros escolhidos foram: {valores}")
        break
print("=-="*7)
print("CADASTRO TERMINADO!")

# NB: SEMPRE TER ATENCAO `A INDENTACAO, E' FULCAR PARA O ANDAMENTO CORECTO DO PROGRAMA.