# Tentavivas de login: Acrescente um atributo chamado login_attempts `a sua classe User do Exercicio 9.3. Escreva um metodo chamado increment_login_attempts() que incremente o valor de login_attempts em 1. Escreva outro metodo chamado reset_login_attempts() que reinicie o valor de login_attempts com 0.
# Crie uma instancia da classe User e chame increment_login_attempts() varias vezes. Exiba o valor de login_attempts para garantir que ele foi incrementado de forma apropriada e, em seguida, chame reset_login_attempts(). Exiba login_attempts nvamente para garantir que seu valor foi reiniciado com 0.
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
            
login = User('herminio', 'alves', 29, 'matola', 'm')
print("=="*20)
login.increment_login_attempts(1)
login.increment_login_attempts(1)
login.increment_login_attempts(1)
login.increment_login_attempts(1)
print(login.login_attempts)
login.reset_login_attempts()
print(login.login_attempts)
        