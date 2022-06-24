"""Classe usavel para representar um restaurante."""

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
        print("="*42)
        print("{:^41}".format("DESCRIBING THE RESTAURANT"))
        print("="*42)
        print(f"|NAME: {self.name:^34}|\n|TYPE: {str(self.type):^34}|".title())
        print("="*42)

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
    def show_number_served(self):
        """Print formatado de todos clientes ja atendidos"""
        print("="*42)
        print("{:^41}".format("SERVED CLIENTS"))
        print("="*42)
        print(f"|| {self.name}: {self.number_served}".title())
        print("="*42)
        
class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ['mango', 'banana', 'stranberry', 'orange', 'baunilha']
    
    def showIceCream_list(self):
        print("=="*15)
        print("\t*FLAVORS MENU*")
        print("=="*15)
        for flavor in self.flavors:
            print(f"-> {flavor}".title())
        print("=="*15)