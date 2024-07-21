from model.entity.sim_card import SimCard
from model.service.sim_card_service import SimcardService
from model.tools.decoratoor import exception_handling


class SimCardController:
    @classmethod
    @exception_handling
    def save(cls,number, operator, status, sim_type, charge):
        sim_card = SimCard(number, operator, status, sim_type, charge)
        SimcardService.save(sim_card)
        return True, SimcardService.save(sim_card)


    @classmethod
    @exception_handling
    def edit(cls,id, number, operator, status, sim_type, charge):
        sim_card = SimCard(id, number, operator, status, sim_type, charge)
        sim_card.id = id
        return True, SimcardService.edit(sim_card)



    @classmethod
    @exception_handling
    def remove(cls,id):
        return True, SimcardService.remove(id)

    @classmethod
    @exception_handling
    def findAll(cls):

        return True, SimcardService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls,id):
        return True, SimcardService.find_by_id()

    @classmethod
    @exception_handling
    def find_by_number(cls,number):
        return True, SimCardController.find_by_number(number)

    @classmethod
    @exception_handling
    def find_by_operator(cls,operator):
        return True, SimCardController.find_by_operator(operator)


    @classmethod
    @exception_handling
    def find_by_sim_type(cls,sim_type):
        return True, SimCardController.find_by_sim_type(sim_type)
