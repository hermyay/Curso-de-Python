# Faca um programa que jogue par ou impar com o computador. O jogo so sera interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep
v = 0
while True:

    # SECCAO RECEPCAO DE DADOS (JOGADOR E COMPUTADOR)
    try:
        print("="*40)
        jogador = int(input("Escolha um numero de 0 a 10: "))
        sleep(1)
    except ValueError:
        print("ERRO DE VALOR: Digite um numero Inteiro!")
    else:
        if jogador > 10 or jogador < 0:
            print("POR FAVOR, ESCOLHA NUMEROS ENTRE 0 E 10.")
        else:
            computador = randint(0,10)
            
    # SECCAO ADICAO DOS DADOS (DO JOGADOR E DO COMPUTADOR)
            adicao = jogador + computador

        # SECCAO DE ESCOLHA ENTRE PAR OU IMPAR (JOGADOR)
            tipo = " "
            while tipo not in "PI":
                tipo = input("Escolhe PAR ou IMPAR [P/I]: ").strip().upper()[0]
                sleep(1)
                if tipo not in "PI":
                    print("Por Favor, escolha PAR ou IMPAR [P/I].")
                else:
                    print("="*40)
                    print(f"ESCOLHEU NUMERO {jogador}\nO COMPUTADOR NUMERO {computador}\nNO TOTAL DEU {adicao}")
                    sleep(1)
                print("="*40)
                sleep(4)

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
            sleep(4)

    # SECCAO DEMONSTRACAO DAS VITORIAS (RANKING)
print("="*40)
sleep(2)
if v < 2:
    print("FIM DE JOGO!!!")
elif v < 4:
    print(f"FIM DE JOGO!!!\nVENCEU APENAS {v} VEZES.")
elif v <= 6:
    print(f"FIM DE JOGO!!!\nPARABENS, VOCE VENCEU {v} VEZES.")
else:
    print(f"FIM DE JOGO!!!\nVOCE E' INCRIVEL NESTE JOGO\nTENS UM TOTAL DE {v} VITORIAS.")
print("="*40)
