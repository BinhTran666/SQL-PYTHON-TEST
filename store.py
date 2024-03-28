from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update
from sqlalchemy import delete

Base = declarative_base()



class Person(Base):
    __tablename__ = 'people'

    id = Column("ID",Integer, primary_key=True)
    fullname = Column("FULLNAME",String)

    def __init__(self, id, fullname):
        self.id = id
        self.fullname = fullname
    def __repr__(self):
        return f"({self.id})  {self.fullname}"        

# Can add more classes here

engine = create_engine("sqlite:///sample.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()