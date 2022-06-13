class Car():
    """Uma tentativa simples de representar um carro."""
    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem um carro."""
        self.make = make
        self.model = model
        self.year = year
        # Trabalhar com valores default
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Desenvolve um nome descritivo, formatado de modo elegante."""
        long_name = str(f"{self.year} {self.make} {self.model}")
        return long_name.title()

    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro"""
        print(f"This car has {str(self.odometer_reading)} miles on it.")

    # Modoficando o valor de um atributo com metodo
    def update_odometer(self, mileage):
        """Define o valor de leitura do hodometro com o valor especificado.
        Regeita a alteracao se for tentativa de definir um valor menor para o hodometro."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

        # Incrementando o valor de um atributo com um metodo
    def increment_odometer(self, miles):
        """ma a quantidade especificada ao valor de leitura do hodometro."""
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# Modoficando o valor de um atributo directamente
my_new_car.odometer_reading = 23

# Saida do valor default
my_new_car.read_odometer()

#
print("=="*20)
#

# Saida do incremento de valor
my_used_car = Car('suburu', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()