# Pessoas atendidas: Comece com seu programa do Exercicio 9.1. Acrescente um atributo chamado number_served cujo valor default e' 0. Crie uma instancia chamada restaurant a partir dessa classe. Apresente o numero de clientes atendidos pelo restaurante e, em seguida, mude esse valor e exiba-o novamente.
# Adicione um metodo chamado set_number_served() que permita definir o numero de clientes atendidos. Chame esse metodo com um novo numero e mostre o valor novamente.
# Acrescente um metodo chamado increment_number_served() que permita incrementar o numero de clientes servidos. Chame esse metodo com qualquer numero que voce quiser e que represente quantos clientes foram atendidos, por exemplo, em um dia de funcionamento.

class Restaurant():
    """Criacao de um restaurante."""
    def __init__(self, name, type):
        """Atributos do restaurante: name e type, valor default => number_served = 0."""
        self.name = name
        self.type = type
        # Atributo valor default 0
        self.number_served = 0
        
    def describle_restaurant(self):
        """Descricao do nome e tipo de restaurante"""
        print(f"\tNAME: {self.name}.\n\tTYPE: {str(self.type)}.".title())

    def open_restaurant(self):
        """Mensagem elegante de que o restaurante esta' aberto."""
        print(f"The restaurant it's now Open!")
        
    # Metodo de definicao do numero de clientes atendidos
    def set_number_served(self, set):
        """Definicao de numero de clientes atendidos. Um atributo."""
        self.number_served = set
        
    # Metodo de incrementacao do numero de clientes
    def increment_number_served(self, new_ones):
        """Incrementacao do numero de clientes. Um atributo."""
        self.number_served += new_ones

# Instancia restaurant
restaurant = Restaurant('nirvana','vegan')
print("=="*20)
# Apresentacao de clientes atendidos
print(restaurant.number_served)
# Mudanca do valor
restaurant.number_served = 20
# Segunda apresentacao de clientes atendidos
print(restaurant.number_served)
# Chamada do metodo de definicao
restaurant.set_number_served(40)
# Mostra do valor do metodo de definicao
print(restaurant.number_served)
# Chamada do metodo de incremento
restaurant.increment_number_served(18)
print(f"Today was served {restaurant.number_served} clients.")