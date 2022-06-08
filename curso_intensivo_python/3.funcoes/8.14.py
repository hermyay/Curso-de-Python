# Carros: Escreva uma funcao que armazene informacoes sobre um carro em um dicionario. A funcao sempre deve receber o nome de um fabricante e um modelo. Um numero arbitrario de argumentos nomeados entao devera ser aceito. Chame a funcao com as informacoes necessarias e dois outros pares nome-valor, por exemplo, uma cor ou um opcional. Sua funcao deve ser apropriada para uma chamada como esta:
# car = make_car('subaru','outback','color='blue',tow_package=True)
# Mostre o dicionario devolvido para garantir que todas as informacoes foram armazenadas correctamente.


def car_info(maker,model,type_automatic,**other_info):
    """Armazena informacoes sobre um carro em um dicionario"""
    info = dict()
    info['manufacturer'] = maker
    info['model'] = model
    for key, value in other_info.items():
        info[key] = value
    if type_automatic in 'Aa':
        info['type automatic'] = True
    elif type_automatic in 'Mm':
        info['type automatic'] = False
    else:
        info['type_automatic'] = 'Unknown!'
    return info


m = str(input("Manufacturer: "))
mo = str(input("Model: "))
t = str(input("[A] for Automatic\n[M] for Manual\n: "))

car = car_info(m,mo,t, color = str(input("Color: ")), motor = str(input("Motor: ")))

for key, value in car.items():
    print("=="*20)
    print(f"\t{key}:\t{value}".upper())
print("=="*20)
print(car)


