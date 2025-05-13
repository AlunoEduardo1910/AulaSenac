#Se for uma função ou variável, nomear tudo em minúsculo e a separação com _
#Se for uma classe, letra inicial maiúscula e a separação é começar a nova palavra com letra maiúscula. Ex: CursoAlunos
#Se for uma variável global, tudo em letra maiúscula

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
        pass