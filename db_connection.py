from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def get_engine(database_url='sqlite:///tax_info.db'):
    return create_engine(database_url)

def get_session(engine):
    DBSession = sessionmaker(bind=engine)
    return DBSession()

engine = get_engine()
session = get_session(engine)