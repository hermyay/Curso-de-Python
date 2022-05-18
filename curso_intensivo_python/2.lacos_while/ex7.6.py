# Tres saidas: Escreva versoes diferentes do Exercicio 7.4 ou do Exercicio 7.5 que faca o seguinte, pelo menos uma vez:
# use um teste condicional na instrucao while para encerrar o laco;
# use uma variavel active para controlar o tempo que o laco executara;
# use uma instrucao break para sair do laco quando o usuario fornecer o valor 'quit'

# Ex 7.4
# Igredientes para uma pizza: Escreva um laco que peca ao usuario para fornecer uma serie de igredientes para uma pizza ate o valor 'quit' seja fornecido. A medida que cada igrediente e' especificado, apresente uma mensagem informando que voce acrescentara' esse igrediente `a pizza.

pizza = ""

while True:
    pizza = str(input("Input the pizza igredient...\n'quit' when your're finished: "))
    if pizza == 'quit':
        print("All igredients added.")
        break
    else:
        print("Next igredient...")