import moeda

p = float(input("Digite o preco do producto: MZN$"))

print(f"O dobro de {moeda.moeda(p)} e' {moeda.moeda(moeda.dobro(p))}")
print(f"A metade de {moeda.moeda(p)} e' {moeda.moeda(moeda.metade(p))}")
print(f" Taxa de -10% e' {moeda.moeda(moeda.diminuir(p, 10))}")
print(f" Taxa de +10% e' {moeda.moeda(moeda.aumentar(p, 10))}")
