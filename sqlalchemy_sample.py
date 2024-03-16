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



engine = create_engine("sqlite:///sample.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_person(person):
    session.add(person)

def update_person(person):
    update_statement = update(Person).where(Person.id == person.id).values(fullname = person.fullname)
    session.execute(update_statement)
# need a Person object with the same id of the person you want to update with different name

def delete_person(id):
    delete_statement = delete(Person).where(Person.id == id)
    session.execute(delete_statement)
# id of the person you want to delete

def find_person(id):
    result = session.query(Person).filter(Person.id == id)
    return result
# id of the person you want to find 


person = Person(13455,"Tran Duc Binh")
person1 = Person(46597,"Nguyen Viet Bang")
person2 = Person(51531,"Le Quoc Khoi")
person3 = Person(14896,"Tran Thuy Van")
person4 = Person(61189,"Bao Tran")

session.add(person)
session.add(person1)
session.add(person2)
session.add(person3)
session.add(person4)


#delete_person(51531)
#add_person(person2)
replacement = Person(51531, "Khoi Quoc Le")
#find_person(51531)
update_person(replacement)
session.commit() 
results = session.query(Person).all()
for r in results:
    print(r)


