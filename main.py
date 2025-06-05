from DataBase.Config import engine
from DataBase.Base import Base
from Tables.usuarios import Usuario
from DataBase.Config import Session

Base.metadata.create_all(engine)
session = Session()


