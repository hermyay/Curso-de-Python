"""Criacao de um usuario"""

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