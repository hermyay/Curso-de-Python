# Ferias dos sonhos: Escreva um programa que faca uma enquete sobre as ferias dos sonhos dos usuarios. Escreva um prompt semelhante a este: Se pudesse visitar um lugar do mundo, para onde voce iria? Inclua um bloco de codigo que apresente os resultados da enquete.
from time import sleep

result = dict()
while True:
    n = str(input("Name: ").title())
    place = str(input(f"{n}, if you could visit a place in the world...\nWould cold be? ").title())
    result[n] = place
    question = str(input("Like to continue? [S/N] "))
    data = result
    while question not in 'SsNn':
        print("Only [S/N] arguments are availeble.")
        question = str(input("Like to continue? [S/N] "))
        if question in 'Nn':
            break    
    if question in 'Nn':
        break
for k, v in result.items():
    print(f"{k} like to visit {v}.")
    sleep(2)
print(data)