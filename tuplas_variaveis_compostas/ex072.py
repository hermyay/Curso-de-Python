# Crie um programa que tenha uma tupla totalmente preechida com uma contagem por extenso, de zero ate' vinte.
# Seu programa devera' ler um numero pelo teclado (entre 0 e 20) e mostra'-lo por extenso.

valor = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "desasseis", "dezassete", "dezoito", "dezanove", "vinte")

while True:
    print("="*50)
    n = int(input("Digite um numero entre 0 e 20 e saiba o seu valor em extenso: "))
    print("="*50)
    if 0 <= n <= 20:
        print(f"Voce digitou o numero {valor[n].title()}.")
    else:
        print("VALOR IRRECONHECIDO!\nPor favor, escolha um numero entre 0 e 20.")
    print("="*50)
    q = input("Deseja continuar?[S/N]: ").upper()
    print("="*50)
    if q in "nN":
        break
    elif q not in "SsnN":
        print("Por favor, digite S para Sim e N para Nao: ").upper()