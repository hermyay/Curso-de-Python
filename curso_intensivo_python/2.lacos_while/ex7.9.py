# Sem pastrami: Usando a lista sandwich_orders do ex7.8, garanta que o sanduiche de 'pastrami' apareca na lista pelo menos tres vezes. Acrescente um codigo proximo ao inicio de seu programa para exibir uma mensagem informando que a lanhonete esta' sem pastrami e, entao, use um laco while para remover todas as ocorrencias de 'pastrami' e sandwiche_orders. Garanta que nunhum sanduiche de pastrami acabe em finished_sandwiches.
from time import sleep

sandwich_orders = ['atum', 'pastrami', 'chiken', 'biff', 'pastrami', 'pork', 'vegan', 'pastrami']
finished_sandwiches = list()

print("\tPS: We havent pastrami today.")

while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    sandwich_request = sandwich_orders.pop()
    finished_sandwiches.append(sandwich_request)
    print(f"{sandwich_request} was requested.")
    sleep(2)
    print("It's been prepared...")
    sleep(2)
    print(f"{sandwich_request} was given.")
    sleep(2)
    print("=="*20)

del sandwich_orders
print(f"All ordered sandwich: {finished_sandwiches}")
print("=="*20)