from model.entity.sim_card import SimCard
from model.da.da import DataAccess


class SimcardService:
    @classmethod
    def save (cls,sim_card):
        sim_card_da = DataAccess(SimCard)
        sim_card_da.save(sim_card)
        return sim_card


    @classmethod
    def edit(cls,sim_card):
        sim_card_da = DataAccess(SimCard)
        sim_card_da.edit(sim_card)
        return sim_card


    @classmethod

    def remove(cls,id):
        sim_card_da = DataAccess(SimCard)
        return sim_card_da.remove(id)


    @classmethod
    def find_all(cls):
        sim_card_da = DataAccess(SimCard)
        return sim_card_da.find_all()

    @classmethod
    def find_by_id(cls,id):
        sim_card_da = DataAccess(SimCard)
        return sim_card_da.find_by_id(id)

    @classmethod
    def find_by(cls,number):
        sim_card_da = DataAccess(SimCard)
        return sim_card_da.find_by(SimCard.number == number)


    @classmethod
    def find_by(cls,operator):
        sim_card_da = DataAccess(SimCard)
        return sim_card_da.find_by(SimCard.operator == operator)

    @classmethod
    def find_by(cls,sim_type):
        sim_card_da = DataAccess(SimCard)
        return sim_card_da.find_by(SimCard.sim_type == sim_type)
