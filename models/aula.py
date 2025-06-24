from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Aula(Base):
    __tablename__ = 'aula'
    id = Column(Integer, primary_key=True, autoincrement=True)
    professor = Column(ForeignKey('professor.id'))
    titulo = Column(String)
    materia = Column(String)
    check_in_id = Column(ForeignKey('aluno.id')) #foreign key
    comentarios_id = Column(ForeignKey('comentario.id')) #foreign key
    material_id = Column(ForeignKey('material.id')) #foreign key
    provas_id = Column(ForeignKey('provas.id')) #foreign key