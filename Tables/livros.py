from sqlalchemy import Column, Integer, String, Boolean
from DataBase.Base import Base

class Livro(Base):
    __tablename__ = 'livros'
    id = Column(Integer, autoincrement=True, primary_key=True)
    titulo = Column(String(100))
    autor = Column(String(100))
    disponivel = Column(Boolean, default = True)