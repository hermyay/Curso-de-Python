# Numeros favoritos: Use um dicionario para armazenar os numeros favoritos de algumas pessoas. Pense em cinco nomes e use-os como chaves em seu dicionario. Pense em um numero favorito para casa pessoa e armazene cada um como um valor em seu dicionario. Exiba o nome de cada pessoa e seu numero favorito. Para que seja mais divertido ainda, faca uma enquete com alguns amigos e obtenha alguns dados reais para o seu programa.

favorite_numbers = dict()
favorite_numbers["Jaoa"] = 12
favorite_numbers["Alberto"] = 4
favorite_numbers["Stelio"] = 34
favorite_numbers["Dilmas"] = 7
favorite_numbers["Paulo"] = 12

for key,valor in favorite_numbers.items():
    print(f"O numero favorito de {key} e' {valor}.")

print(favorite_numbers)