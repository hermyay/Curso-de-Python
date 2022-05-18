# Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com os nomes de varios sanduiches. Em seguida, crie uma lista vazia chamada finished_sandwiches. Percorra a lista de pedidos de sanduiches com um laco e mostre uma mensagem para cada pedido, por exemplo, Preparei seu sanduiche de atum. A medida que cada sanduiche for preparado, transfira-o para a lista de sanduiche prontos. Depois que todos os sanduiches estiverem prontos, mostre uma mensagem que liste cada sanduiche preparado.

from time import sleep


sandwich_orders = ['atum','chiken','biff', 'pork', 'vegan']
finished_sandwiches = list()

while sandwich_orders:
    sandwich_request = sandwich_orders.pop()
    print(f"{sandwich_request} was requested.")
    sleep(2)
    print("It's been prepared...")
    sleep(2)
    finished_sandwiches.append(sandwich_request)
    print(f"{sandwich_request} was given.")
    sleep(2)
    print("=="*20)

print(f"All ordered sandwich: {finished_sandwiches}")
print("=="*20)