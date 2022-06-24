# Admin: Um administrador e' um tipo especial de usuario. Escreva uma classe chamada Admin que herde da classe User escrita no Exercicio 9.3, ou do Exercicio 9.5. Adicione um atributo privileges que armazene uma lista de strings como "can add post", "can delete post", "can ban user", e assim por diante. Escreva um metodo chamado show_privileges() que liste o conjunto de privilegios de um administrador. Crie uma instancia de Admin e chame seu metodo.

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
    def __init__(self, first_name, last_name, age, location, gender):
        super().__init__(first_name, last_name,age, location, gender)
        self.previleges = ['can add posts', 'can delete posts', 'can ban users']
    
    def show_priveleges(self):
        print("=="*20)
        print("The Administrator have this priveleges:")
        print("=="*20)
        for previlege in self.previleges:
            print(f"--> The Administrator, {previlege}.")
        print("=="*20)

admin = Admin('herminio', 'alves', 29, 'matola', 'male')
admin.show_priveleges()