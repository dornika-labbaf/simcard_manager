from model.entity.person import Person
from model.service.person_service import PersonService
from model.tools.decoratoor import exception_handling


class PersonController:
    @classmethod
    @exception_handling
    def save(cls, name, family, nid, date_birth, father_name, email, address):
        person = Person(name, family, nid, date_birth, father_name, email, address)
        return True, PersonService.save(person)

    @classmethod
    @exception_handling
    def edit(cls, id, name, family, nid, date_birth, father_name, email, address):
        person = Person(id, name, family, nid, date_birth, father_name, email, address)
        person.id = id
        return True, PersonService.edit(person)

    @classmethod
    @exception_handling
    def remove(cls, id):
        return True, PersonService.remove(id)

    @classmethod
    @exception_handling
    def findAll(cls):
        return True, PersonService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, PersonService.find_by_id()

    @classmethod
    @exception_handling
    def find_by_family(cls, family):
        return True, PersonService.find_by_family(family)

    @classmethod
    @exception_handling
    def find_by_nid(cls, nid):
        return True, PersonService.find_by_nid(nid)

    @classmethod
    @exception_handling
    def find_by_email(cls, email):
        return True, PersonService.find_by_email(email)

    @classmethod
    @exception_handling
    def find_by_address(cls, address):
        return True, PersonService.find_by_address(address)
