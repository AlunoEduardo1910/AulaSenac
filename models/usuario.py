from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    nascimento = Column(Date, nullable=False)
    genero = Column(String)
    email = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    cidade = Column(String)
    estado = Column(String)
    pais = Column(String)
    cep = Column(String)

class Professor(Usuario):
    __tablename__ = 'professor'
    materia = Column(String)
    curso_id = Column(Integer, ForeignKey('curso.id')) #foreign key
    aulas_id = Column(Integer, ForeignKey('aula.id')) #foreign key

class Aluno(Usuario):
    __tablename__ = 'aluno'
    cursos_id = Column(Integer, ForeignKey('curso.id'))
    em_progresso = Column(Integer, ForeignKey('prova.id'))
    aulas_id = Column(Integer, ForeignKey('aula.id')) #foreign key
    materias = Column(String)
    provas_id = Column(Integer, ForeignKey('prova.id')) #foreign key
