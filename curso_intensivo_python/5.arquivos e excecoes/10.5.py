# Enquete sobre programacao: Escreva um laco while que pergunte 'as pessoas por que elas gostam de programacao. Sempre que alguem fornecer um motivo, acrescente-o em um arquivo que armazene todas as respostas.
while True:
    question = str(input("Wy do you like programing? "))
    with open('entrevist.txt', 'a') as file_object:
        file_object.write(f"{question}\n")
    break_question = str(input("Continue? "))
    while break_question not in 'sSnN':
        break_question = str(input("ERROR.\nContinue?[S/N]: "))
        if break_question in 'nN':
            break
    if break_question in 'nN':
        break