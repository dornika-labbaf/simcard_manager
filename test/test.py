from datetime import datetime

from model.da.da import DataAccess
from model.entity import Person
from model.entity import SimCard
from model.entity import payment


person = Person("ali","alipour","1234567890", datetime.now())
person_da = DataAccess(Person)
person_da.save(person)
print(person)

sim_card = SimCard("09038952277","irancell","daemi","ffff","etebari")
sim_card_da = DataAccess(SimCard)
sim_card_da.save(sim_card)
print(sim_card)

