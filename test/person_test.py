from datetime import datetime
from model.tools.validator import *
from controller.person_controller import PersonController
#controller=PersonController
PersonController.save(5,"mmd","0150253400", datetime.now(),
                "mmd","mmd@gmail.com","idk")
#person = Person("ali","alipour","1234567890", datetime.now(),"ahmad","@dornika.email.com","lll5")
#person_da = DataAccess(Person)
#person_da.save(person)
#print(person)