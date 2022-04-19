# Crie um programa que tenha uma funcao factorial() que receba dois parametros: o primeiro que indique o numero a calcular e o outro chamado show, que sera' um valor logico (opcional) indicando se sera' mostrado ou nao na tela o processo de calculo do factorial.

def factorial(n, show=False):
	f = 1
	for contador in range(n, 0, -1):
		if show:
			print(contador,end="")
			if contador > 1:
				print(f" x",end=" ")
			else:
				print(f" =",end=" ")
		f *= contador
	return f

# Programa Principal
print(factorial(5, show=True))				
