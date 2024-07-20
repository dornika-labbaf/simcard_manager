from model.da.da import DataAccess
from model.entity import Person
from datetime import datetime
person = Person("ali","alipour","1234567890", datetime.now(),"ahmad","@dornika.email.com","lll5")
person_da = DataAccess(Person)
person_da.save(person)
print(person)