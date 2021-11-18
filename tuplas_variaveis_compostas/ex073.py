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
for pos in range(len(chap[6])):
    print(pos)
print("=-="*20)
for pos in chap[6]:
    print(pos)
print("=-="*20)
for pos in enumerate(chap[6]):
    print(f"O Ajax esta' na {pos} posicao.")