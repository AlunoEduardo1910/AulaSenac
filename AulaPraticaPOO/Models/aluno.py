import datetime
from uuid import uuid4



class Aluno:

    #ATRIBUTOS

    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento
        self.matricula = str(uuid4())
        self.ingresso = datetime.datetime.now()
        self.curso = None
        self.notas = []

    #COMPORTAMENTOS

    def marcar_prova(self, data_prova, nome_prova):
        prova = {}
        prova.get(nome_prova)

        if not prova:
            raise Exception

        prova["data"]= data_prova
        prova["aluno"] = self.matricula

        return f"Sua prova foi marcada para o dia {data_prova} com sucesso."

    def fazer_media(self):
        if not self.notas:
            return "Nenhuma nota foi encontrada"

        media = sum(self.notas)/len(self.notas)

        return f"Sua média é de {media}"

    def repor_aula(self, nome_aula, data_reposicao):
        aulas_perdidas = {}
        aula = aulas_perdidas.get(nome_aula)

        if not aula:
            return "Você já fez essa aula."

        aula["Aula_reposicao"] = data_reposicao
        aula["Aluno"] = self.matricula

        return f"Sua aula foi marcada para o dia {data_reposicao}"





