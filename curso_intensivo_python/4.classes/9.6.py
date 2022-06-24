# Sorveteria: Uma sorveteria e' um tipo especifico de restaurante. Escreva uma classe chamada IceCreamStand que herde da classe Restaurant escrita no Exercicio 9.1 ou no Exercicio 9.4. Qualquer versao da classe funcionara; basta escolher aquela de que voce mais gosta. Adicione um atributo chamado flavors que armazene uma lista de sabores de sorvete. Escreva um metodo para mostrar esses sabores. Crie uma instancia de IceCreamStand e chame esse metodo.

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
            
iceCream = IceCreamStand('Starbuck', 'Restaurant')
iceCream.showIceCream_list()
            