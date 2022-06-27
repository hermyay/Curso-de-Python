# Dados: O modulo random contem funcoes que geram numeros aleatorios de varias maneiras. A funcao randint() devolve um inteiro no intervalo especificado por voce. O codigo a seguir devolve um numero entre 1 e 6:
from random import randint
x = randint(1, 6)
# Crie uma classe Die com um atributo chamado sides, cujo valor default e' 6. Escreva um metodo chamado roll_die() que exiba um numero aleatorio entre 1 e o numero de lados do dado. Crie um dado de seis lados e lance-o dez vezes. Crie um dado de dez lados e outro de vinte lados. Lance cada dado dez vezes.

class Die():
    def __init__(self, sides = 6):
        self.sides = sides
    print("=="*20)
    
    def roll_die(self):
        print(f"Aleatory number betwen 1 - 6: {randint(1, self.sides)}")
        print("="*40)
        
        print(f"\t6 sides 10 times trown:")
        for  self.c in range(0, 10):
            self.c = randint(1, 6) 
            print(f"{self.c}",end=' - ')
        print("\n")
        print("=="*20)
        
        print("\t10 sides 10 times trown:")
        for self.c in range(0, 11):
            self.c = randint(1, 10)
            print(f"{self.c}",end=' - ')
        print("\n")
        print("=="*20)
        
        print("\t20 sides 10 times trown:")
        for self.c in range(0, 11):
            self.c = randint(1, 20)
            print(f"{self.c}",end=' - ')
        print("\n")
        print("=="*20)
            
dados = Die()
dados.roll_die()