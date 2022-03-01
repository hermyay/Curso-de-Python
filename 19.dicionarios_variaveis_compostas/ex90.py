# Faca um programa que leia o nome e a media de um aluno e guarde, tambem, a situacao em um dicionario. No final, mostre o conteudo da estrutura na tela.
aluno = dict()
aluno['nome'] = str(input("Nome do Aluno: ").title().strip())
aluno['media'] = float(input(f"Media do aluno, {aluno['nome']}: "))
if 9.5 <= aluno['media'] <= 20:
    aluno['situacao'] = "Aprovado"
elif 0 <= aluno['media'] < 9.5:
    aluno['situacao'] = "Reprovado"
else:
    aluno['situacao'] = "ERRO!!! AS NOTAS VAO DE 0 'A 20 VALORES"

print(aluno)

print("-=-"*20)

print(f"O Aluno, {aluno['nome'].upper()} esta': {aluno['situacao'].upper()}.")

print("-=-"*20)
