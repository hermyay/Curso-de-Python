def dobro(preco = 0):
    resp = preco * 2
    return resp

def metade(preco = 0):
    resp = preco / 2
    return resp

def diminuir(preco = 0, taxa = 0):
    resp = preco - (preco * taxa/100)
    return resp

def aumentar(preco = 0, taxa = 0):
    resp = preco + (preco * taxa/100)
    return resp

def moeda(preco = 0, moeda = "MZN$"):
    return f"{moeda}{preco:>5.2f}".replace(".",",")