# Upgrade de bateria: Use a ultima versao de electric_car.py desta seccao. Acrescente um metodo chamado upgrade_battery() na classe Battery. Esse metodo deve verificar a capacidade da bateria e defini-la com 85 se o valor for diferente. Crie um carro electrico com uma capacidade de bateria default, chame get_range() uma vez e, em seguida, chame get_range() uma segunda vez apos fazer um upgrade da bateria. Voce devera ver um aumento na distancia que o carro e' capaz de percorrer.

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = str(f'{self.year} {self.make} {self.model}')
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")
        
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = f"This car can go approximately {range}\nmiles on a full charge."
        print(message)
        
    def upgrade_battery(self, battery_size = 85):
        self.battery_size = battery_size

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
        self.battery = Battery()
        
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")
        
    def fill_gas_tank():
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.get_range()