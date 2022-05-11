# Ingressos para o cinema: Um cinema cobra precos diferentes para os ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos de 3 anos de idade, o ingresso sera' gratuito; se tiver entre 3 e 12 anos, o ingresso custara' 10 dolares; se tiver mais de 12 anos; o ingresso custara' 15 dolares. Escreva um laco em que voce pergunte a idade aos usuarios e, entao, informe-lhes o preco do ingresso do cinema.

age = " "
while age != 999:
    age = int(input("Please, tell me your age: "))
    if  age == 999:
        print("Ended Program.")
    elif age < 3:
        print("Your have a free ticket.")
        print("Dial '999' to quit.")
    elif age > 2 and age < 13:
        print("Your ticket will cost 10 dolares.")
        print("Dial '999' to quit.")
    elif age > 12:
        print("Your ticket will cost 15 dolares.")
        print("Dial '999' to quit.")

    