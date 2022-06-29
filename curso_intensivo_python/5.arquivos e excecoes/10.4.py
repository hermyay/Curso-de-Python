# Lista de convidados: Escreva um laco while que pergunte o nome aos usuarios. Quando fornecerem seus nomes, apresente uma saudacao na tela e acrescente uma linha que registre a visita do usuario em um arquivo chamado guest_book.txt. Certifique-se de que cada entrada esteja em uma nova linha do arquivo.
while True:
    user = str(input("Your name: "))
    with open('guest_book', 'a') as file_object:
        file_object.write(f"User visit: {user}\n")
    print(f"Hi, {user}. Wellcome to the program.")
    print("=="*20)
    question = str(input("Continue? "))
    while question not in 'sSnN':
        question = str(input("ERROR.\nContinue?[S/N]: "))
        if question in 'nN':
            break
    if question in 'nN':
        break
    
    