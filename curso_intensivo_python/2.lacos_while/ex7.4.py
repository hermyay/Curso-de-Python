# Igredientes para uma pizza: Escreva um laco que peca ao usuario para fornecer uma serie de igredientes para uma pizza ate o valor 'quit' seja fornecido. A medida que cada igrediente e' especificado, apresente uma mensagem informando que voce acrescentara' esse igrediente `a pizza.

igredient = " "

while igredient != "quit":
    igredient = str(input("Please, dial the igrendients\nOne at the time: "))
    
    if igredient == 'quit':
        print("All igredients add.")
    else:
        print(f"Igredient {igredient} added.\nIf is the last one, please input 'quit'")