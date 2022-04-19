# Crie um programa que tenha a funcao leiaInt(), que vai funcionar de forma semelhante 'a funcao input() do Python,so que fazendo a validaço para aceitar apenas um valor numerico. Ex: n = leiaInt('Digite um n')

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok =True
        else:
            print('ERRO! Digite um numero inteiro valido.')
        if ok:
            break
    return valor

# Programa Principal
n = leiaInt("Digite um numero: ")
print(f"Numero digitado: {n}.")
