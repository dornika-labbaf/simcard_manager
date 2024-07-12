from model.entity.person import Person
from model.da.da import DataAccess


class PersonService:
    @staticmethod
    def save(person):
        person_da = DataAccess(Person)
        person_da.save(person)
        return person

    @staticmethod
    def edit(person):
        person_da = DataAccess(Person)
        person_da.edit(person)
        return person

    @staticmethod
    def remove(id):
        person_da = DataAccess(Person)
        return person_da.remove(id)

    @staticmethod
    def find_all():
        person_da = DataAccess(Person)
        return person_da.find_all()

    @staticmethod
    def find_by_id(id):
        person_da = DataAccess(Person)
        return person_da.find_by_id(id)

    @staticmethod
    def find_by(family):
        person_da = DataAccess(Person)
        return person_da.find_by(Person.family == family)

    @staticmethod
    def find_by(nid):
        person_da = DataAccess(Person)
        return person_da.find_by(Person.nid == nid)

    @staticmethod
    def find_by(email):
        person_da = DataAccess(Person)
        return person_da.find_by(Person.email == email)

    @staticmethod
    def find_by(address):
        person_da = DataAccess(Person)
        return person_da.find_by(Person.address == address)
