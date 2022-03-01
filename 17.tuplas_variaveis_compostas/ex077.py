# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

print("=="*30)
print(f"{'DEMONSTRAÇÃO DE VOGAIS':^60}")
print("=="*30)
palavra = "ambíguo", "literatura", "arte", "constragimento", "acção", "paixão", "severidade", "oito"
for pal in palavra:
    print(f"\nNa palavra {pal.title()}, existem as vogais: ",end="")
    for cada in pal:
        if cada in "aãeiíou":
            print(cada,end=" ")
            
    print("\n")
    print("=="*30)