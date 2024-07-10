from model.entity.sim_card import SimCard
from model.da.da import DataAccess
from mvc.controller.exeptions.exeptions import SimCardNotFoundError


class SimcardService:
    @staticmethod
    def save (sim_card):
        sim_card_da = DataAccess(SimCard)
        sim_card_da.save(sim_card)
        return sim_card


    @staticmethod
    def edit(sim_card):
        sim_card_da = DataAccess(SimCard)
        sim_card_da.edit(sim_card)
        return sim_card


    @staticmethod

    def remove(id):
        sim_card_da = DataAccess(SimCard)
        sim_card_da.remove(id)


    @staticmethod
    def find_all():
        sim_card_da = DataAccess(SimCard)
        return sim_card_da.find_all()

    @staticmethod
    def find_by_id(id):
        sim_card_da = DataAccess(SimCard)
        return sim_card_da.find_by_id(id)

