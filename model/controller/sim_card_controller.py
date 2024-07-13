from model.entity.sim_card import SimCard
from model.service.sim_card_service import SimcardService
from model.tools.logger import Logger


class SimCardController:
    @staticmethod
    def edit(id, number, operator, status, sim_type, charge):
        try:
            sim_card = SimCard(id, number, operator, status, sim_type, charge)
            sim_card.id = id
            SimcardService.edit(sim_card)
            Logger.info(f"sim card edit - {sim_card}")
            return True, sim_card
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def save(number, operator, status, sim_type, charge):
        try:
            sim_card = SimCard(number, operator, status, sim_type, charge)
            sim_card.id = id
            SimcardService.save(sim_card)
            Logger.info(f"sim card save - {sim_card}")
            return True, sim_card
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def remove(id):
        try:
            sim_card = SimcardService.remove(id)
            Logger.info(f"sim card remove - {sim_card}")
        except Exception as e:
            Logger.error(f"{e}")

    @staticmethod
    def findAll():
        try:
            sim_card_list = SimcardService.find_all()
            Logger.info(f"sim card findAll")
            return True, sim_card_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_id(id):
        try:
            sim_card = SimcardService.find_by_id()
            Logger.info(f"sim card find by id({id})")
            return True, sim_card
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_number(number):
        try:
            sim_card_list = SimCardController.find_by_number(number)
            Logger.info(f"Sim card find by number({number})")
            return True, sim_card_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_operator(operator):
        try:
            sim_card_list = SimCardController.find_by_number(operator)
            Logger.info(f"Sim card find by operator({operator})")
            return True, sim_card_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"


    @staticmethod
    def find_by_sim_type(sim_type):
        try:
            sim_card_list = SimCardController.find_by_sim_type(sim_type)
            Logger.info(f"Sim card find by sim_type({sim_type})")
            return True, sim_card_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"
