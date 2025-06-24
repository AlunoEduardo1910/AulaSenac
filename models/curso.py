from tkinter.constants import CASCADE

from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Curso(Base):
    __tablename__ = 'curso'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    materias = Column(String, nullable=False)
    alunos_id = Column(Integer, ForeignKey('aluno.id')) #foreign key
    comentarios_id = Column(Integer, ForeignKey('comentario.id')) #foreign key
    aulas_id = Column(Integer, ForeignKey('aula.id')) #foreign key