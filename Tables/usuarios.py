from sqlalchemy import Column, Integer, String
from DataBase.Base import Base


class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, autoincrement=True, primary_key=True)
    nome = Column(String(100))
    email = Column(String(100))


