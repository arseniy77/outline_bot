from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declared_attr, declarative_base, Session

from src import settings

class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)

class User(Base):

    name = Column(String, unique=True)
    password = Column(String)
    port = Column(String)
    method = Column(String)
    accessUrl = Column(String)
    data_usage = Column(Integer, nullable=True)

    def __str__(self):
        return f'Пользователь {self.name}, id {self.id}'

engine = create_engine(settings.DATABASE_URL, echo=True)
session = Session(engine)