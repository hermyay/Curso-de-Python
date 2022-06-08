class dog():
    """Uma tentativa simples de modelar um cao."""
    def __init__(self, name, age):
        """Inicializa os atributos name e age."""
        self.name = name
        self.age = age

    def sit(self):
        """Simula um cao a sentar em resposta a um comando."""
        print(f"{self.name.title()} is now sitting.")
    
    def roll_over(self):
        """Simula um cao a rolar em resposta a um comando."""
        print(f"{self.name.title()} rolled over!")

my_dog = dog('willie', 6)

print(f"My dog's name is {my_dog.name.title()}")
print(f"My dog is {str(my_dog.age)} years old.")

my_dog.sit()
my_dog.roll_over()

your_dog = dog('lucy', 3)

print(f"Your dog's name is {your_dog.name.title()}.")
print(f"Your dog is {str(your_dog.age)} years old.")
your_dog.sit()
your_dog.roll_over()