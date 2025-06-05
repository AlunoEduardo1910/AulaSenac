from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import foreign

from DataBase.Base import Base

class Emprestimo(Base):
    __tablename__ = 'emprestimos'
    id = Column(Integer, autoincrement=True,primary_key=True)
    usuario_id = (Integer, ForeignKey('usuarios.id'))
    livro_id = (Integer, ForeignKey('livros.id'))
    data_emprestimo = Column(DateTime)
    data_devolucao  = Column(DateTime, nullable=False)