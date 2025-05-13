from AulaPraticaPOO.app.logica_sistema import cadastrar_aluno, listar_alunos

comando = ""
while comando != "3":
    comando = input(f"Escolha uma opção: \n"
                    f"1) Cadastrar Alunos\n"
                    f"2) Listar Alunos \n"
                    f"3) Sair do sistema \n")

    match comando:
        case "1":
            nome = input("Informe o nome do aluno: ")
            nascimento = input("Informe a data de nascimento do aluno: ")
            curso = input("Informe o curso do aluno, caso tenha, se não, deixe vázio: ")

            print(cadastrar_aluno(nome, nascimento, curso))

        case "2":
            print(listar_alunos())

        case "3":
            print("Saindo do sistema.")
