# Numeros favoritos: Modifique o seu programa do Exercicio 02.py para que cada pessoa possa ter mais de um numero favorito. Em seguida, apresente o nome de cada pessoa, juntamente com seus numeros favoritos.

favorite_numbers = dict()
favorite_numbers["Jaoa"] = [12, 23, 45, 14, 75, 43]
favorite_numbers["Alberto"] = [4, 8, 2, 18, 14, 12]
favorite_numbers["Stelio"] = [34, 89, 56, 84, 34, 66, 43]
favorite_numbers["Dilmas"] = [7, 8, 6, 5, 3, 1, 0]
favorite_numbers["Paulo"] = [12]

for k, v in favorite_numbers.items():
    if len(v) == 1:
        print(f"{k} favorite number is: {v}". title())
    else:
        print(f"{k} favorite numbers are: {v}".title())