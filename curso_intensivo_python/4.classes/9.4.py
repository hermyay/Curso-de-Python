# Pessoas atendidas: Comece com seu programa do Exercicio 9.1. Acrescente um atributo chamado number_served cujo valor default e' 0. Crie uma instancia chamada restaurant a partir dessa classe. Apresente o numero de clientes atendidos pelo restaurante e, em seguida, mude esse valor e exiba-o novamente.
# Adicione um metodo chamado set_number_served() que permita definir o numero de clientes atendidos. Chame esse metodo com um novo numero e mostre o valor novamente.
# Acrescente um metodo chamado increment_number_served() que permita incrementar o numero de clientes servidos. Chame esse metodo com qualquer numero que voce quiser e que represente quantos clientes foram atendidos, por exemplo, em um dia de funcionamento.

class Restaurant():
    """Um restaurante."""
    def __init__(self, restaurant_name, cuisine_type):
        """Atributos do restaurante."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describle_restaurant(self):
        print(f"The Restaurant it's named as {self.restaurant_name.title()}\nWith {str(self.cuisine_type)} cuisine.\nThe restaurant has served {self.number_served} people.")
        

    def open_restaurant(self):
        print(f'The "{self.restaurant_name.title()}" restaurant its now Open!')

    def set_number_served(self, set_number):
        if set_number >= self.number_served:
            self.number_served = set_number
            print(f"The Restaurant it's named as {self.restaurant_name.title()}\nWith {str(self.cuisine_type)} cuisine.\nThe restaurant has served {self.number_served} people.")
        else:
            print(f"The Restaurant it's named as {self.restaurant_name.title()}\nWith {str(self.cuisine_type)} cuisine.\nERROR: The numbers of served clients can only increase.\nThe {set_number} clients served are uncontible.")
    def increment_number_served(self, clients):
        self.number_served += clients

restaurant = Restaurant('Good Food', 17)
print(restaurant.describle_restaurant())
'''
restaurant.number_served = 45
print(restaurant.describle_restaurant())

print("=="*20)

restaurant.number_served = 60
print(restaurant.describle_restaurant())

print("=="*20)

restaurant.set_number_served(59)

print("=="*20)

restaurant.set_number_served(90)

print("=="*20)


while restaurant.set_number_served(0):
    client = input("New client number: ")
    question = input(str("Another one? "))
    if question in "nN":
        break

restaurant.set_number_served(client)
'''