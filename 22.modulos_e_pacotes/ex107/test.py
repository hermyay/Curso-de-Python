import moeda

p = float(input("Digite o preco do producto: $"))

print(f"O dobro de {p}$ e' {moeda.dobro(p)}$")
print(f"A metade de {p}$ e' {moeda.metade(p)}$")
print(f" Taxa de -10% de {p} e' {moeda.diminuir(p, 10)}")
print(f" Taxa de +10% de {p} e' {moeda.aumentar(p, 10)}")
