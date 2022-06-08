# Tres restaurantes: Comece com a classe do Exercicio 9.1. Crie tres instancias diferentes da classe e chame describe_restaurant() para cada instancia.
from restaurant import Restaurant

print("=="*20)
your_restaurant = Restaurant("melhor pizza", 10)
your_restaurant.describle_restaurant()
your_restaurant.open_restaurant()
print("=="*20)
edgar_restaurant = Restaurant('mangancas', 45)
edgar_restaurant.describle_restaurant()
edgar_restaurant.open_restaurant()
print("=="*20)
cobica_restaurant = Restaurant('dos cotas', 99)
cobica_restaurant.describle_restaurant()
cobica_restaurant.open_restaurant()
print("=="*20)