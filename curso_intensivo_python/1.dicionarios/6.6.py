# Pessoas: Comece com o programa que voce escreveu no ex01.py. Crie dois novos dicionarios que representem pessoas diferentes e armazene os tres dicionarios em uma lista chamada people. Percorra sua lista de pessoas com um laco. `A medida que percorrer a lista, apresente tudo que voce sabe sobre cada pessoa.
'''
people = {}
people_list = list()

for k in range(3):
    people["first_name"] = str(input("Nome:").title())
    people["last_name"] = str(input("Sobrenome: ").title())
    people["age"] = int(input("Idade: "))
    people["city"] = str(input("Cidade: ").title())
    people_list.append(people.copy())

for p in people_list:
    for v in people.values():
        print("=="*20)
        print(f"Nome: {v}\nSobrenome: {v}\nIdade: {v}\nCidade: {v}")
        print("=="*20)
'''
# Outra forma de resolucao mais fiel ao exercicio.
pessoas = list()

new_pessoa1 = {'nome': 'herminio', 'sobrenome': 'alves', 'idade': '29', 'cidade':'matola'}
pessoas.append(new_pessoa1)
new_pessoa2 = {'nome': 'adalberto', 'sobrenome': 'matsinhe', 'idade': '40', 'cidade':'gaza'}
pessoas.append(new_pessoa2)
new_pessoa3 = {'nome': 'sofia', 'sobrenome': 'zavene', 'idade': '26', 'cidade':'zavala'}
pessoas.append(new_pessoa3)

for pessoa in pessoas:
    print(f"Nome: {pessoa['nome']}\nSobrenome: {pessoa['sobrenome']}\nIdade: {pessoa['idade']}\nCidade: {pessoa['cidade']}".title())