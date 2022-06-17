# Restaurante: Crie uma classe chamada Restaurant. O metodo __init__() de Restaurant deve armazenar dois atributos: restaurant_name e cuisine_type. Crie um metodo chamado describe_restaurant() que mostre essas duas informacoes, e um metodo de nome open_restaurant() que exiba uma mensagem informando que o restaurante esta aberto.

# PS: A classe Restaurant se encontra no Modulo restaurant.py. o mesmo foi importado na resolucao deste exercicio. 

class Restaurant():
    """Um restaurante."""
    def __init__(self, name, type):
        """Atributos do restaurante."""
        self.name = name
        self.type = type
    
    def describle_restaurant(self):
        print(f"\tNAME: {self.name.title()}.\n\tTYPE: {str(self.type)}.")

    def open_restaurant(self):
        print(f"The restaurant it's now Open!")

restaurant = Restaurant('iFood', 'vegan')
print("=="*20)
print(f"My restaurant name is {restaurant.name}.\nIt's a {restaurant.type} restaurant.")
restaurant.describle_restaurant()
restaurant.open_restaurant()
print("=="*20)