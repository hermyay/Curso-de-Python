# Enquete: Utilize o codigo em favorite_language.py
# Crie uma lista de pessoas que devam participar da enquete sobre linguagem favorita. Inclua alguns nomes que ja' estejam no dicionario e outros que nao estao.
# Percorra a lista de pessoas que devem participar da enquete. Se elas ja tiverem respondido `a enquete, mostre uma mensagem agradecendo-lhe por responder. Se ainda nao participaram da enquete, apresente uma mensagem convidando-as a responder.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'chefe': 'javascript',
    'edgar': 'php'
}

list_name = ['edgar', 'marcia','jen', 'augusto', 'retirante', 'sarah', 'chefe', 'madalena', 'joao', 'goza-montinho']

for key in list_name:
    if key in favorite_languages:
        print(f"Muito obrigado por sua resposta, {key}.")
        print("=="*20)
    elif key not in favorite_languages:
        print(f"{key}, por favor, responda a questao.")
        print("=="*20)