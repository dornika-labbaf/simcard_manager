from model.da.da import DataAccess
from model.entity import SimCard

sim_card = SimCard("09038952277", "irancell", "daemi", "ffff", "etebari")
sim_da = DataAccess(SimCard)
sim_da.save(sim_card)
print(sim_card)