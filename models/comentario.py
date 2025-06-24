from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Comentario(Base):
    __tablename__ = 'comentario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(25))
    descricao = Column(String)
    data_comentario = Column(String)
    aula = Column(String) #foreign key
    curso = Column(String) #foreign key
    aluno = Column(String) #foreign key
    anonimo = Column(Boolean, default=False)
