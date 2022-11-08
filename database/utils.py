import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

logging.basicConfig()
logging.getLogger('sqlalchemy.dialects.postgresql').setLevel(logging.INFO)

engine = create_engine(
    "postgresql+psycopg2://postgres:password@localhost:5432/postgres",
    isolation_level="SERIALIZABLE",
)


def get_db_connection():
    return engine.connect()


def get_session():
    return sessionmaker(bind=engine)
