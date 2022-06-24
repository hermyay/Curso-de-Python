# Varios modulos: Armazene a classe User em um modulo e as Classes Privileges e Admin em um modulo separado. Em outro arquivo, crie uma instancia de Admin e chame show_privileges() para mostrar que tudo continua funcionando de forma apropriada.
import administrator
print("=="*20)
name = str(input("Name: "))
last_name = str(input("Last Name: "))
age = int(input("Age: "))
location = str(input("Location: "))
gender = str(input("Gender: "))
new_user = administrator.Admin(name,last_name,age,location,gender)
new_user.show_priveleges()