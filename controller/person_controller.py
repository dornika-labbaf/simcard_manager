from model.entity.person import Person
from model.service.person_service import PersonService
from model.tools.logger import Logger


class PersonController:
    @staticmethod
    def edit(id, name, family, nid, date_birth, father_name, email, address):
        try:
            person = Person(id, name, family, nid, date_birth, father_name, email, address)
            person.id = id
            PersonService.edit(person)
            Logger.info(f"person edit - {person}")
            return True, person
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def save(name, family, nid, date_birth, father_name, email, address):
        try:
            person = Person(name, family, nid, date_birth, father_name, email, address)
            person.id = id
            PersonService.save(person)
            Logger.info(f"person save - {person}")
            return True, person
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def remove(id):
        try:
            person = PersonService.remove(id)
            Logger.info(f"person remove - {person}")
        except Exception as e:
            Logger.error(f"{e}")

    @staticmethod
    def findAll():
        try:
            person_list = PersonService.find_all()
            Logger.info(f"person findAll")
            return True, person_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_id(id):
        try:
            person = PersonService.find_by_id()
            Logger.info(f"person by id({id})")
            return True, person
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_family(family):
        try:
            person_list = PersonService.find_by_family(family)
            Logger.info(f"person find by family({family})")
            return True, person_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_nid(nid):
        try:
            person_list = PersonService.find_by_nid(nid)
            Logger.info(f"person find by nid({nid})")
            return True, person_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_email(email):
        try:
            person_list = PersonService.find_by_email(email)
            Logger.info(f"person find by email({email})")
            return True, person_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_address(address):
        try:
            person_list = PersonService.find_by_address(address)
            Logger.info(f"person find by address({address})")
            return True, person_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"
