from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from DataBase.Base import Base

engine = create_engine("mysql+pymysql://root:root@localhost:3306/biblioteca")

Session = sessionmaker(bind=engine)
