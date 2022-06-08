# Usuarios: Crie uma classe chamada User. Crie dois atributos de nomes first_name e last_name e, entao, crie varios outros atributos normalmente armazenados em um perfil de usuario. Escreva um metodo de nome describe_user() que apresente um resumo das informacoes do usuario. Escreva outro metodo chamado great_user() que mostre uma saudacao personalizada ao usuario.
# Crie varias instacias que representem diferentes usuarios e chame os dois metodos para cada usuario.
from users import User

for k in range(0,4):
    f_name = str(input("User First Name: "))
    l_name = str(input("User Last Name: "))
    print("=="*20)
    users = User(f_name, l_name)
    users.describe_user()
    users.great_user()
    print("=="*20)