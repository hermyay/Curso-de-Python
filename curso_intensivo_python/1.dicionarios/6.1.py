# Pessoa: Use um dicionario para armazenar informacoes sobre uma pessoa que voce conheca. Armazene seu primeiro nome, o sobrenome, a idade e a cidade em que ela vive. Voce devera ter chaves como first_name, last_name, age e city.
print("=="*20)
print("        PESSOA QUE CONHECO")
print("=="*20)
people = {}

people["first_name"] = str(input("Nome:").title())
people["last_name"] = str(input("Sobrenome: ").title())
people["age"] = int(input("Idade: "))
people["city"] = str(input("Cidade: ").title())
print("=="*20)
print(f"Informacoes sobre {people['first_name']}: {people}.")
print("=="*20)

