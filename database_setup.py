from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class TaxInfo(Base):
    __tablename__ = 'tax_info'
    id = Column(Integer, primary_key=True)
    income = Column(String, nullable=False)
    expenses = Column(String, nullable=False)

engine = create_engine('sqlite:///tax_info.db')
Base.metadata.create_all(engine)
