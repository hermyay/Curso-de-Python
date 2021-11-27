# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []
while True:
    n = int(input("Digite um valor: "))
    if n not in valores:
        valores.append(n)
    else:
        print("O valor já foi adicionado.")
    perg = input(str("Quer continuar? [S/N]: ")).strip().upper()[0]
    while perg not in "SsNn":
        perg = input(str("Por favor, digite Sim ou Nao.\nQuer continuar? [S/N]: ")).strip().upper()[0]
    if perg in "Nn":
        print("=-="*20)
        print(f"Os numeros escolhidos foram: {valores}")
        break
print("GAME OVER!")