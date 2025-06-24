from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from usuario import Professor

Base = declarative_base()

class Prova(Base):
    __tablename__ = 'prova'
    id = Column(Integer, primary_key=True, autoincrement=True)
    curso_id = Column(Integer, ForeignKey('curso.id'))
    material = Column(String)
    titulo = Column(String(25))
    descricao = Column(String)
    nota = Column(Integer)
    questoes_id = Column(Integer, ForeignKey('questoes.id')) #foreign key

class Questao(Base):
    __tablename__ = 'questoes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    texto = Column(String)
    respostas = Column(String)
    resposta_correta = Column(String)