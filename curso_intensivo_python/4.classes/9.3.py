# Usuarios: Crie uma classe chamada User. Crie dois atributos de nomes first_name e last_name e, entao, crie varios outros atributos normalmente armazenados em um perfil de usuario. Escreva um metodo de nome describe_user() que apresente um resumo das informacoes do usuario. Escreva outro metodo chamado great_user() que mostre uma saudacao personalizada ao usuario.
# Crie varias instacias que representem diferentes usuarios e chame os dois metodos para cada usuario.

class User():
    """Usuarios do site."""
    def __init__(self, first_name, last_name, age, location, gender):
        """Inicializa os atributos do usuario."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.gender = gender
    
    def describe_user(self):
        """Resumo das informacoes do usuario."""
        print(f"USER NAME: {self.first_name} {self.last_name}.\nUSER AGE: {self.age}\nUSER GENDER: {self.gender.upper()[0]}".title())

    def great_user(self):
        """Mostra uma saudacao personalizada ao usuario."""
        print(f"Dear, {self.first_name}. Welcome!!!".title())

for k in range(0,4):
    f_name = str(input("User First Name: "))
    l_name = str(input("User Last Name: "))
    age = int(input("User Age: "))
    location = str(input("User Location: "))
    gender = str(input("User gender: "))
    print("=="*20)
    users = User(f_name, l_name, age, location, gender)
    users.describe_user()
    print("=="*20)
    users.great_user()
    print("=="*20)