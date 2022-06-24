# Tres restaurantes: Comece com a classe do Exercicio 9.1. Crie tres instancias diferentes da classe e chame describe_restaurant() para cada instancia.
from restaurants import Restaurant

print("=="*20)
your_restaurant = Restaurant("melhor pizza", "take away")
your_restaurant.describle_restaurant()
print("=="*20)
edgar_restaurant = Restaurant('mangancas', 'vegan')
edgar_restaurant.describle_restaurant()
print("=="*20)
cobica_restaurant = Restaurant('dos cotas', 'regular')
cobica_restaurant.describle_restaurant()
print("=="*20)