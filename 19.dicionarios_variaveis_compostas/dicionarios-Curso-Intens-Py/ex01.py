# Pessoa: Use um dicionario para armazenar informacoes sobre uma pessoa que voce conheca. Armazene seu primeiro nome, o sobrenome, a idade e a cidade em que ela vive. Voce devera ter chaves como first_name, last_name, age e city.
people = {}
question = ""
while question not in "sS":
    first_name = str(input("Nome:").title())
    last_name = str(input("Sobrenome: ").title())
    age = int(input("Idade: "))
    city = str(input("Cidade: ").title())
    question = str(input("Continuar? [S/N] ").upper()[0])
    if question == "nN":
        break
    else:
        question = str(input("ERROR! Apenas valores [S] ou [N]\nContinuar? [S/N] "))
