# Faca um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario. O programa sera interrompido quando o numero solicitado for negativo.

while True:
    n = int(input("Digite um numero: "))
    print("="*40)
    if n < 0:
        break
    for c in range (1,11):
        print(f"{n} x {c} = {n*c}")
    print("="*40)
print("FIM DA TABUADA")