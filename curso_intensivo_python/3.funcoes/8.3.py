# Camiseta: Escreva uma funcao chamada make_shirt() que aceite um tamanho e o texto de uma mensagem que devera' ser estampada na camiseta. A funcao deve exibir uma frase que mostre o tamanho da camiseta e a mensagem estampada.

# ARGUMENTOS POSICIONAIS
def make_shirt(size, msg):
    cont = len(msg)
    print("=="*20)
    print(f"The requested shirt has '{size}' size and '{msg}' as a mensage whit {cont} caracters.".strip())
    print("=="*20)

make_shirt('M','Love Python')

# ARGUMENTOS NOMEADOS

make_shirt(size='M', msg='Love Python')