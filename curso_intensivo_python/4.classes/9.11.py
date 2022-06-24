# Importando Admin: Comece com seu programa do Exercicio 9.8. Armazene as classes User, Privileges e Admin em um modulo. Crie um arquivo separado e uma instancia de Admin e chame show_privileges() para mostrar que tudo esta funcionando de forma apropriada.

import users

print("=="*20)
name = str(input("Name: "))
last_name = str(input("Last Name: "))
age = int(input("Age: "))
location = str(input("Location: "))
gender = str(input("Gender: "))

first_login = users.Admin(name,last_name,age,location,gender)
first_login.show_priveleges()
first_login = users.User(name,last_name,age,location,gender)
first_login.describe_user()