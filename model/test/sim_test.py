from model.da.da import DataAccess
from model.entity import SimCard
from controller.sim_card_controller import SimCardController
#sim_card = SimCard("09038952277", "irancell", "daemi", "ffff", "etebari")
#sim_da = DataAccess(SimCard)
#sim_da.save(sim_card)
#print(sim_card)
SimCardController.save("09038952277", "irancell", "daemi", "ffff", "etebari")