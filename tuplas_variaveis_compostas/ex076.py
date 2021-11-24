# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequêcia.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

# Minha resolucao
print("--"*20)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("--"*20)
precos = "Pão", 10.00, "Leite", 100.00, "Sumo", 85.00, "Yougurt", 35.00, "Jam", 200.00, "Cornofleks", 250.00, "Bolachas", 80.00, "Custard", 85, "Feijão", 100.00, "Manteiga", 55.00
print(f"{precos[0]:.<30} MZN$ {precos[1]:.2f}")
print(f"{precos[2]:.<30} MZN$ {precos[3]:.2f}")
print(f"{precos[4]:.<30} MZN$ {precos[5]:.2f}")
print(f"{precos[6]:.<30} MZN$ {precos[7]:.2f}")
print(f"{precos[8]:.<30} MZN$ {precos[9]:.2f}")
print(f"{precos[10]:.<30} MZN$ {precos[11]:.2f}")
print(f"{precos[12]:.<30} MZN$ {precos[13]:.2f}")
print(f"{precos[14]:.<30} MZN$ {precos[15]:.2f}")
print(f"{precos[16]:.<30} MZN$ {precos[17]:.2f}")
print(f"{precos[18]:.<30} MZN$ {precos[19]:.2f}")
print("--"*20)

# Do professor

print("-"*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("-"*40)
for pos in range(0, len(precos)):
    if pos % 2 == 0:
        print(f"{precos[pos]:.<30}",end="")
    else:
        print(f"MZN${precos[pos]:>7.2f}")
print("-"*40)
