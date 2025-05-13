from AulaPraticaPOO.Models.aluno import Aluno

CURSOS = {}
ALUNOS = []

def cadastrar_aluno(nome, nascimento, curso=None):

    if not nome or not nascimento:
        return "Parâmetros inválidos"

    c = {}
    aluno_obj = Aluno(nome, nascimento)

    if curso:
        c = CURSOS.get("curso")
        c("alunos").append(aluno_obj)


    ALUNOS.append(aluno_obj)


    return {
        "nome_aluno": aluno_obj.nome,
        "matricula": aluno_obj.matricula,
        "curso": c.get("nome_curso")
    }

def listar_alunos():
    resposta = ""
    for aluno in ALUNOS:
        resposta += (f"Nome: {aluno.nome} \n"
                     f"Matrícula: {aluno.matricula} \n"
                     f"Curso: {aluno.curso} \n"
                     f"------------------------- \n")

    return resposta


