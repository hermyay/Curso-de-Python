"""Cria um usuario administrador | Garante os previlegios do usuario."""

class Admin():
    def __init__(self, first_name, last_name, age, location, gender, previleges = ['can add posts', 'can delete posts', 'can ban users']):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.gender = gender
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