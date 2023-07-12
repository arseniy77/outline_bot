from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import (Session, declarative_base, declared_attr,
                            relationship)

from src import settings


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    id = Column(Integer, primary_key=True, index=True)


Base = declarative_base(cls=PreBase)


class User(Base):

    name = Column(String, unique=True)
    password = Column(String)
    port = Column(String)
    method = Column(String)
    accessUrl = Column(String)
    data_usage = Column(Integer, nullable=True)
    admin_tg_id = Column(Integer, ForeignKey('admin.id'))
    admin = relationship('Admin', back_populates='users')

    def __str__(self):
        return f'Пользователь {self.name}, id {self.id}'


class Admin(Base):
    admin_tg_id = Column(Integer, nullable=False)
    users = relationship('User', cascade='delete', back_populates='admin')


engine = create_engine(settings.DATABASE_URL, echo=True)
session = Session(engine)
