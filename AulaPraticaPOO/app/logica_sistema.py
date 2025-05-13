from AulaPraticaPOO.Models.aluno import Aluno

CURSOS = {}
ALUNOS = {}

def cadastrar_aluno(nome, nascimento, nome_curso=None):

    if not nome or not nascimento:
        return "Parâmetros inválidos"

    c = None
    aluno_obj = Aluno(nome, nascimento)

    if nome_curso:
        c = CURSOS.get(nome_curso)
        c.alunos[aluno_obj.matricula] = aluno_obj


    ALUNOS[aluno_obj.matricula] = aluno_obj


    return {
        "nome_aluno": aluno_obj.nome,
        "matricula": aluno_obj.matricula,
        "curso": c.nome or None
    }

def listar_alunos():
    resposta = ""
    for aluno in ALUNOS.values():
        resposta += (f"Nome: {aluno.nome} \n"
                     f"Matrícula: {aluno.matricula} \n"
                     f"Curso: {aluno.curso.nome or "Sem curso no momento"} \n"
                     f"------------------------- \n")

    return resposta

def detalhar_aluno(matricula):
    if not matricula:
        return "Parametros Inválidos"

    aluno = ALUNOS.get(matricula)

    if not aluno:
        return "Aluno não cadastrado"

    return (f"Nome: {aluno.nome} \n"
            f"Matrícula: {aluno.matricula} \n"
            f"Data de nascimento: {aluno.nascimento} \n"
            f"Data de ingresso: {aluno.ingresso} \n"
            f"Curso: {aluno.curso.nome or "Sem curso no momento"} \n"
            f"Notas: {aluno.notas}")

def deletar_aluno(matricula):
    if not matricula:
        return "Parametros Inválidos"

    aluno = ALUNOS.get(matricula)

    if not aluno:
        return "Aluno não cadastrado"

    if aluno.curso:
        curso = CURSOS.get(aluno.curso.nome)
        curso.alunos.pop(matricula)

    ALUNOS.pop(matricula)

    return f"Aluno {aluno.nome} excluído com sucesso."

