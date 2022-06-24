# Importando Restaurant: Usando sua classe Restaurant mais recente, armazene-a em um modulo. Crie um arquivo separado que importe Restaurant. Crie uma instancia de Restaurant e chame um de seus metodos para mostrar que a instrucao import funciona de forma apropriada.

import restaurants

first_restaurant = restaurants.Restaurant('starBucks', 'fast food')
second_restaurant = restaurants.Restaurant('KFC', 'Dailly Meal')
first_restaurant.describle_restaurant()
second_restaurant.describle_restaurant()
first_restaurant.set_number_served(2)
first_restaurant.increment_number_served(20)
first_restaurant.show_number_served()
second_restaurant.set_number_served(40)
second_restaurant.show_number_served()
#help(restaurant)