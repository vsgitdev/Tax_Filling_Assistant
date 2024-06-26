# database_setup.py

from sqlalchemy import Column, Integer, Float
from db_connection import Base, get_engine

class TaxInfo(Base):
    __tablename__ = 'tax_info'
    id = Column(Integer, primary_key=True)
    income = Column(Float, nullable=False)
    expenses = Column(Float, nullable=False)

engine = get_engine()
Base.metadata.create_all(engine)
