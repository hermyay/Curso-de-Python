# Restaurante: Crie uma classe chamada Restaurant. O metodo __init__() de Restaurant deve armazenar dois atributos: restaurant_name e cuisine_type. Crie um metodo chamado describe_restaurant() que mostre essas duas informacoes, e um metodo de nome open_restaurant() que exiba uma mensagem informando que o restaurante esta aberto.

# PS: A classe Restaurant se encontra no Modulo restaurant.py. o mesmo foi importado na resolucao deste exercicio. 

from restaurant import Restaurant

my_restaurant = Restaurant('iFood', 12)
print("=="*20)
my_restaurant.describle_restaurant()
my_restaurant.open_restaurant()
print("=="*20)