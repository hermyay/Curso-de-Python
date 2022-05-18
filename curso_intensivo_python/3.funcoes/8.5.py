# Cidades: Escreva uma funcao chamada describe_city() que aceite o nome de uma cidade e seu pais. A funcao deve exibir uma frase simples, como Reyjavik esta' localizada na Islandia. Forneca um valor default ao parametro que representa o pais. Chame sua funcao para tres cidades diferentes em que pelo menos uma delas nao esteja no pais default.

def describle_city(city_name, country = 'South Africa'):
    '''Show the name of city and is country
    first argument for name and second for country in South Africa default.'''
    print("=="*24)
    print(f"\t{city_name} is located in {country}.".title())
    print("=="*24)

describle_city('capytown')
describle_city('maputo', 'mozambique')
describle_city('sao paulo', 'brasil')