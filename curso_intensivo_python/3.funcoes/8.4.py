# Camisetas grandes: Modifique a funcao make_shirt() de modo que as camisetas sejam grandes por default, com uma mensagem Eu amo Python. Crie uma camiseta grande e outra media com a mensagem default, e uma camiseta de qualquer tamanho com uma mensagem diferente.

# Valores por default
def make_shirt(size = ('XL'), msg = 'I Love Python'):
    '''Making a T'shirt. Firts argument for 'size' in XL default and second for message 'msg' in I Love Python default.
    Sizes: 'S' to small | 'M' to medium | 'L' to Large and 'XL' to extra large. '''
    cont = len(msg)
    if size in "Ss":
        size = 'small'
    elif size in "Mm":
        size = 'medium'
    elif size in "Ll":
        size = 'large'
    elif size in 'XLxl':
        size = 'extra large'
    else:
        print("Indefined argument.")
    print("=="*20)
    print(f"\tSize of the shirt: {size}\n\tMessage: {msg}.\n\tNumber of caracters: {cont}.".title())
    print("=="*20)

# Camiseta grande e outra media com mensagem default.
make_shirt('L')
make_shirt('M')

# Camiseta de qualquer tamanho com mensagem diferente.
make_shirt('s', 'Python is The Best')