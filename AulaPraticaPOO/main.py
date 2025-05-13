from AulaPraticaPOO.app.logica_sistema import cadastrar_aluno, listar_alunos, detalhar_aluno, deletar_aluno

comando = ""
while comando != "5":
    comando = input(f"Escolha uma opção: \n"
                    f"1) Cadastrar Alunos\n"
                    f"2) Listar Alunos \n"
                    f"3) Detalhar Aluno \n"
                    f"4) Deletar Aluno \n"
                    f"5) Sair \n")

    match comando:
        case "1":
            nome = input("Informe o nome do aluno: ")
            nascimento = input("Informe a data de nascimento do aluno: ")
            curso = input("Informe o curso do aluno, caso tenha, se não, deixe vázio: ")

            print(cadastrar_aluno(nome, nascimento, curso))

        case "2":
            print(listar_alunos())

        case "3":
            matricula = input("Informa a matrícula do aluno: ")

            print(detalhar_aluno(matricula))

        case "4":
            matricula = input("Informa a matrícula do aluno: ")

            print(deletar_aluno(matricula))

        case "5":
            print("Saindo do sistema.")
