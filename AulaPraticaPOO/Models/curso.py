#Se for uma função ou variável, nomear tudo em minúsculo e a separação com _
#Se for uma classe, letra inicial maiúscula e a separação é começar a nova palavra com letra maiúscula. Ex: CursoAlunos
#Se for uma variável global, tudo em letra maiúscula
from AulaPraticaPOO.Models.aluno import Aluno


class Curso:
    def __init__(self, nome, duracao, professor, materias):
        self.nome = nome
        self.alunos = {}
        self.duracao = duracao
        self.professor = professor
        self.materias = materias
        self.aulas = []

    def contabilizar_presenca(self):
        pass

    def listar_alunos_aprovados(self):
        if not Aluno.notas:
            return "Nenhuma nota foi encontrada."
        media = sum(Aluno.notas)/len(Aluno.notas)
        if media >= 9:
            return "Aprovado com excelência"
        elif media < 9 and media > 6:
            return "Aprovado"
        else:
            return "Reprovado"
