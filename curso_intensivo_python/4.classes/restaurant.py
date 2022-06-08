class Restaurant():
    """Um restaurante."""
    def __init__(self, restaurant_name, cuisine_type):
        """Atributos do restaurante."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describle_restaurant(self):
        print(f"The Restaurant it's named as {self.restaurant_name.title()}.")
        print(f"With {str(self.cuisine_type)} cuisine.")

    def open_restaurant(self):
        print(f'The "{self.restaurant_name.title()}" restaurant its now Open!')