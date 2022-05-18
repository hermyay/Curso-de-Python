# Nomes de cidade: Escreva uma funcao chamada city_country() que aceite o nome de uma cidade e seu pais. A funcao deve devolver uma string formatada assim:
  # "Santiago, Chile"
# Chame a sua funcao com pelo menos tres pares cidade-pais e apresente o valor devolvido.

def city_country(city, country):
    '''city names and their country'''
    print("=="*20)
    full = str(f"\t{city}, {country}.")
    print("=="*20)
    return full

result1= city_country('Santiago', 'Chile')
print(result1)
result2 = city_country('Matola', 'Mozambique')
print(result2)
result3 = city_country('CapyTown', 'South Africa')
print(result3)
print("=="*20)