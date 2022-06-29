# Convidado: Escreva um programa que pergunte o nome ao usuario. Quando ele responder, escreva o nome em um arquivo chamado guest.txt.
guests = dict()
guests_list = list()
for user in range(0, 2):
    guests['name'] = str(input("Your name: "))
    guests['last name'] = str(input("Last name: "))
    guests_list.append(guests.copy())

with open('guest.txt', 'a') as file_object:
    file_object.write(f"{guests_list}\n")