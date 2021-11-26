'''
Do contrário das Tuplas que são imutáveis, as Listas são mutáveis. E, em vez de parenteses () que identificam as Tuplas, as Listas levam parenteses rectos [].
'''
# Exemplo de substituição de valores na Lista.
num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)

# Exemplo de adição de valores na Lista.
num.append(7)
print(num)
# Exemplo da organização da Lista usando o método sort()
#NB: O método sort(), organiza a Lista por ordem crescente (tratando-se de numeros) ou por ordem alfabética (tratando-se de palavras).
num.sort()
print(num)


# Exemplo de organização decrescente da Lista usando o método sort(reverse=True)
num.sort(reverse=True)
print(num)

# Exemplo de adição de valor numa especifica variavel da Lista usando o método insert().
num.insert(2, 0)
print(num)

# Exemplo de eliminação do último valor da Lista usando o método pop().
num.pop()
print(num)

# Exemplo de eliminação de um determinado valor usando o método pop()
num.pop(2)
print(num)

# Exemplo de eliminação de um valor na Lista usando o método remove().
#NB: Se a Lista contém dois ou mais valores iguais, ao indicar o valor, apenas o primeiro é removido se não indicada a posição a que a remoção tem de ser feita.
num.remove(5)
print(num)