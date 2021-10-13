# 1. Exemplo de um trecho de codigo sem o uso da interupcao de repeticoes.
num = soma = 0
while num != 90:
    num = int(input("Digite um numero: "))
    soma += num
soma -= 90
print(f"A soma dos valores e' igual a {soma}.")
print("FIM!")

# 2. Com a interupcao de repeticoes while.
n = s = 0
while True:
    n = int(input("Digite um numero: "))
    if n == 90:
        break
    s += n
print(f"A soma dos valores e' igual a: {s}.")
print("FIM!")

# NB: A forma corecta de executar essa operacao e' usando o formato de codigo n.2