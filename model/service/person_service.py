from model.entity.person import Person
from model.da.da import DataAccess
from  controller.exeptions.exeptions import PersonNotFoundError
from model.tools.decoratoor import *

class PersonService:
    @classmethod
    def save(cls,person):
        person_da = DataAccess(Person)
        person_da.save(person)
        return person

    @classmethod
    def edit(cls,person):
        person_da = DataAccess(Person)
        person_da.edit(person)
        return person

    @classmethod
    def remove(cls,id):
        person_da = DataAccess(Person)
        return person_da.remove(id)

    @classmethod
    def find_all(cls):
        person_da = DataAccess(Person)
        return person_da.find_all()

    @classmethod
    def find_by_id(cls,id):
        person_da = DataAccess(Person)
        return person_da.find_by_id(id)

    @classmethod
    def find_by(cls,family):
        person_da = DataAccess(Person)
        return person_da.find_by(Person.family == family)

    @classmethod
    def find_by(cls,nid):
        person_da = DataAccess(Person)
        return person_da.find_by(Person.nid == nid)

    @staticmethod
    def find_by(cls,email):
        person_da = DataAccess(Person)
        return person_da.find_by(Person.email == email)

    @classmethod
    def find_by(cls,address):
        person_da = DataAccess(Person)
        return person_da.find_by(Person.address == address)
