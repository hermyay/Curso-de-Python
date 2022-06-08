class User():
    """Usuarios do site."""
    def __init__(self, first_name, last_name):
        """Inicializa os atributos do usuario."""
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        """Apresenta o nome e o sobrenome do usuario."""
        print(f"The user name is, {self.first_name.title()} {self.last_name.title()}.")

    def great_user(self):
        """Mostra uma saudacao ao usuario."""
        print(f"WellCome, {self.first_name.title()} {self.last_name.title()}")