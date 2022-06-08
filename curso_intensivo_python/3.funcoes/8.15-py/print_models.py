import printing_fuctions

unprinted_designs = list()

for c in range(0, 3):
    designs = str(input("Designs: "))
    unprinted_designs.append(designs)

completed_models = list()

printing_fuctions.print_models(unprinted_designs, completed_models)
printing_fuctions.show_completed_models(completed_models)
print("=="*20)