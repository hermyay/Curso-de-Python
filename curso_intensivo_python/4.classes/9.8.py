# Privilegios: Escreva uma classe Privileges separada. A classe deve ter um atributo privileges que armazene uma lista de strings conforme descrita no Exercicio 9.7. Transfira o metodo show_privileges() para essa classe. Crie uma instancia de Privileges como um atributo da classe Admin. Crie uma nova instancia de Admin e use metodo para exibir os privilegios.
class User():
    """Usuarios do site."""
    def __init__(self, first_name, last_name, age, location, gender):
        """Inicializa os atributos do usuario."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.gender = gender
        self.login_attempts = 0
    
    def describe_user(self):
        """Resumo das informacoes do usuario."""
        print(f"USER NAME: {self.first_name} {self.last_name}.\nUSER AGE: {self.age}\nUSER GENDER: {self.gender.upper()[0]}".title())

    def great_user(self):
        """Mostra uma saudacao personalizada ao usuario."""
        print(f"Dear, {self.first_name}. Welcome!!!".title())
    
    def increment_login_attempts(self, attempts):
        """Faz a conta das vezes em que foi tentado um login."""
        self.login_attempts += attempts
        
    def reset_login_attempts(self):
        """Faz o reset das tentativas de login."""
        if self.login_attempts > 1:
            self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, age, location, gender, previleges = ['can add posts', 'can delete posts', 'can ban users']):
        super().__init__(first_name, last_name,age, location, gender)
        self.previleges = previleges
        self.prev = Privileges()
    
    def show_priveleges(self):
        print("=="*20)
        print("The Administrator have this priveleges:")
        print("=="*20)
        for previlege in self.previleges:
            print(f"--> The Administrator, {previlege}.")
        print("=="*20)
        
class Privileges():
    def __init__(self, privileges = ['can add posts', 'can delete posts', 'can ban users']):
        self.privileges = privileges
    
    def show_priveleges(self):
        print("=="*20)
        print("The Administrator have this priveleges:")
        print("=="*20)
        for previlege in self.privileges:
            print(f"--> The Administrator, {previlege}.")
        print("=="*20)
        
privilege_user = Admin('edgar', 'augusto', 15, 'das mangas', 'male', Privileges())
privilege_user.prev.show_priveleges()