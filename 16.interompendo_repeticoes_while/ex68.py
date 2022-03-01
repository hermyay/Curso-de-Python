# Faca um programa que jogue par ou impar com o computador. O jogo so sera interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.

from random import randint
v = 0
while True:

    # SECCAO RECEPCAO DE DADOS (JOGADOR E COMPUTADOR)
    jogador = int(input("Escolha um numero de 0 a 10: "))
    if jogador > 10 or jogador < 0:
        print("POR FAVOR, ESCOLHA NUMEROS ENTRE 0 E 10")
    else:
        computador = randint(0,10)
    
    # SECCAO ADICAO DOS DADOS (DO JOGADOR E DO COMPUTADOR)
        adicao = jogador + computador

    # SECCAO DE ESCOLHA ENTRE PAR OU IMPAR (JOGADOR)
        tipo = " "
        while tipo not in "PI":
            tipo = input("Escolhe PAR ou IMPAR [P/I]: ").strip().upper()[0]
            if tipo not in "PI":
                print("Por Favor, escolha PAR ou IMPAR [P/I].")
            else:
                print("="*40)
                print(f" ESCOLHEU NUMERO {jogador} \n O COMPUTADOR NUMERO {computador} \n NO TOTAL DA {adicao}")

    # SECCAO SORTEIO
        if tipo == "P":
            if adicao % 2 == 0:
                print("VOCE VENCEU!!!")
                v += 1
            else:
                print("Voce perdeu.")
                break
        elif tipo == "I":
            if adicao % 2 == 1:
                print("VOCE VENCEU!!!")
                v += 1
            else:
                print("Voce perdeu...")
                break
        print("VAMOS JOGAR DE NOVO...")

    # SECCAO DEMONSTRACAO DAS VITORIAS (RANKING)
if v < 2:
    print("FIM DE JOGO!!!")
elif v < 4:
    print(f"FIM DE JOGO!!! \n VENCEU APENAS {v} VEZES.")
elif v <= 6:
    print(f"FIM DE JOGO!!! \n PARABENS, VOCE VENCEU {v} VEZES.")
else:
    print(f"FIM DE JOGO!!! \n VOCE E' INCRIVEL NESTE JOGO \n TENS UM TOTAL DE {v} VITORIAS.")
print("="*40)