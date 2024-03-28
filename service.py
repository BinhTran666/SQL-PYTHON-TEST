from store import*

def add_person(person):
    session.execute("INSERT INTO people (ID, FULLNAME) VALUES (?,?)",(person.id,person.fullname))

def update_person(person):
    session.execute("UPDATE people SET FULLNAME = ? WHERE ID = ?",(person.fullname,person.id))
# need a Person object with the same id of the person you want to update with different name

def delete_person(id):
    session.execute("DELETE FROM people WHERE ID = ?",(id))
# id of the person you want to delete

def find_person(id):
    result = session.execute("SELECT * FROM people WHERE ID = ?",(id))
    return result
# id of the person you want to find 


# person = Person(13455,"Tran Duc Binh")
# person1 = Person(46597,"Nguyen Viet Bang")
# person2 = Person(51531,"Le Quoc Khoi")
# person3 = Person(14896,"Tran Thuy Van")
# person4 = Person(61189,"Bao Tran")

# session.add(person)
# session.add(person1)
# session.add(person2)
# session.add(person3)
# session.add(person4)


#delete_person(51531)
#add_person(person2)
#replacement = Person(51531, "Khoi Quoc Le")
#find_person(51531)
#update_person(replacement)
session.commit() 
results = session.query(Person).all()
for r in results:
    print(r)


