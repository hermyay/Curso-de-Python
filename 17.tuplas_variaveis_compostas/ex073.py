# Crie uma tupla preenchida com os 20 primeiros colocados da tabela da Champions League, na ordem de colocacao. Depois mostre:
# a) Apenas os 5 primeiros colocados.
# b) Os ultimos 4 colocados da tabela.
# c) Uma lista com as equipas em ordem alfabetica.
# d) Em que posicao na tabela esta' a equipa do Ajax.
print("TABELA DOS VINTE PRIMEIROS COLOCADOS DA CHAMPIONS")
chap = ("Real Madrid","Barcelona","Man. City","Chelsea","Dortmund","Juventos","Ajax","Atalanta","Atletico Madrid","Liverpool","Shakhtar Donetsk","Sevilla","Salzburg","Leipzig","Bayern","Benfica","Porto","Man. United","Paris","Villarreal")
print("=-="*20)
print(chap)
print("=-="*20)
print(chap[0:5])
print("=-="*20)
print(chap[16:20])
print("=-="*20)
print(sorted(chap))
print("=-="*20)
p = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
print(f"O {chap[6]} esta' na {p.index(6)}a posicao.")
print("=-="*20)
for pos in range(len(chap[6])):
    print(pos)
print("=-="*20)
for pos in chap[6]:
    print(pos)
print("=-="*20)