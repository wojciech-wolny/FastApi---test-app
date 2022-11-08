from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from database.utils import engine


class TableBase:
    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=TableBase)


class Users(Base):
    __tablename__ = 'users'

    name = Column(String)
    lastname = Column(String)


Base.metadata.create_all(engine)
