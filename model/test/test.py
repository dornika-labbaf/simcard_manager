from datetime import datetime

from model.controller.sim_card_controller import SimCardController
from model.da.da import DataAccess
from model.entity import Person
from model.entity.payment import Payment


#person = Person("ali","alipour","1234567890", datetime.now(),"ahmad","@dornika.email.com","shahrach5")
#person_da = DataAccess(Person)
#person_da.save(person)
#print(person)

#sim_card = SimCard("09038952277","irancell","daemi","ffff","etebari")
#sim_card._owner_id = 5
#sim_card_da = DataAccess(SimCard)
#sim_card_da.save(sim_card)
#print(sim_card)

#payment = Payment("6/5/444",200000,"sim card")
#payment_da = DataAccess(Payment)
#payment_da.save(payment)
#print(payment)

sim_card = SimCardController.save("09038952277","irancell","ok","daemi","55556",)
print(sim_card)
