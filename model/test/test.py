from datetime import datetime

from model.controller.sim_card_controller import SimCardController
from model.da.da import DataAccess
from model.entity import Person, SimCard
from model.entity.payment import Payment
from model.controller.payment_controller import PaymentController
from model.controller.person_controller import PersonController


#person = Person("ali","alipour","1234567890", datetime.now(),"ahmad","@dornika.email.com","shahrach5")
#person_da = DataAccess(Person)
#person_da.save(person)
#print(person)

#sim_card = SimCard("09038952277", "irancell", "daemi", "ffff", "etebari")
#sim_card._owner_id = 5
#sim_card_da = DataAccess(SimCard)
#sim_card_da.save(sim_card)
#print(sim_card)

#payment = Payment("6/5/444",200000,"sim card")
#payment_da = DataAccess(Payment)
#payment_da.save(payment)
#print(payment)

#sim_card = SimCardController.save("09038952277","irancell",True,"daemi","55556",)
#print(sim_card)

#person = PersonController.save("sara","salahi","0150526024","1390/8/6","ali","@dornikagmail.com","sahrack5")
#print(person)

#payment = PaymentController.save("2024/5/8","6000000","sim")
#print(payment)
import unittest
#from model.entity.sim_card import SimCard

class TestSimCard(unittest.TestCase):
    def test_number_validator(self):
        sim_card = SimCard("09038952277","irancell","daemi","ffff","etebari")
        self.assertEqual(sim_card.number, "09038952277")

    def test_invalid_number(self):
        with self.assertRaises(ValueError):
            SimCard("12345","irancell","daemi","ffff","etebari")

    def test_operator_validator(self):
        sim_card = SimCard("09038952277","irancell","daemi","ffff","etebari")
        self.assertEqual(sim_card.operator, "irancell")

    # def test_invalid_operator(self):
    #     with self.assertRaises(ValueError):
    #         SimCard("09038952277","invalid_operator","daemi","ffff","etebari")

if __name__ == '__main__':
    unittest.main()
