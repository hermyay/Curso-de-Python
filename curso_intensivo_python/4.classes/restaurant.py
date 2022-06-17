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