from datetime import datetime

from model.da.da import DataAccess
from model.entity import Person


person = Person("ali","alipour","1234567890", datetime.now())
person_da = DataAccess(Person)
person_da.save(person)
print(person)