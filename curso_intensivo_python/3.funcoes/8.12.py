# Sanduiches: Escreva uma funcao que aceite uma lista de itens que uma pessoa quer numa sanduiche. A funcao deve ter um parametro que agrupe tantos itens quantos forem fornecidos pela chamada da funcao e deve apresentar um resumo do sanduiche pedido. Chame a funcao tres vezes usando um numero diferente de agrupamentos a cada vez.

def sanduiches(topping):
    print(f"Os ingrendientes escolhidos para sanduiche sao: ")
    for v in topping:
        print(f"\t==> {v}")


sandes = list()
question = ""

while True:
    igredients = str(input("Introduza um igrediente para sua sandes: "))
    sandes.append(igredients)
    print("=="*20)
    question = str(input("\t[S] para adicional.\n\t[N] para terminar.\n\t: "))
    if question in 'sS':
        print("Novo igredient...")
    elif question in 'nN':
        print(f"Todos igredients add.")
        break
    while question not in 'SsNn':
        question = str(input("\t[S] para adicional.\n\t[N] para terminar.\n\t: "))

print("=="*20)
sanduiches(sandes)