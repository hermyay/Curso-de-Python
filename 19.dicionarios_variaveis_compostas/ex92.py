# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionario se por acaso a CTPS for diferente de zero, o dicionario recebera' tambem o ano de contratacao e o salario. Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar.
contratado = {
    'nome':str(input("Nome: ")),
    'ano_nascimento':int(input("Ano de Nascimento: ")),
    'carteira_trab':int(input("Carteira de Trabalho nº (0 se nao tem): "))
    }

contratado['idade'] = 2021 - contratado['ano_nascimento']
contratado['ctps'] = contratado['carteira_trab']

if contratado['carteira_trab'] > 0:
    contratado['ano_contratacao'] = int(input("Ano de Contratacao: "))
    contratado['salario'] = float(input("Salario: MZN$ "))
    contratado['aposentadoria'] = (contratado['ano_contratacao'] + 35) - contratado['ano_nascimento']

del contratado['carteira_trab']
del contratado['ano_nascimento']
print("***"*20)
print(contratado)
print("***"*20)
for p, k in contratado.items():
    print(f"{p} : {k}")
print("***"*20)
