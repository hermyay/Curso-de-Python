# Calculadora para adicao: Coloque o codigo do Exercicio 10.6 em um laco while para que o usuario possa continuar fornecendo numeros, mesmo se cometerem um erro e digitarem um texto no lugar de um numero.
numbers = list()
sum = 0
c = 0
while True:
    try:
        c += 1
        user = int(input(f"{c}º number: "))
        numbers.append(user)
        sum += user
    except ValueError:
        print("=="*40)
        print("Value can't be Validated, onlly aceptible integer numbers.")
        print("=="*40)
    else:
        question = str(input("Continue? "))
        while question not in 'yYnN':
            question = str(input("ERROR. Olly [Y/N]: "))
        if question in 'nN':
            break
    
print("=="*40)
print(f"Sum of {numbers} = {sum}")
print("=="*40)
