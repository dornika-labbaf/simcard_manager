from model.entity.payment import Payment
from model.service.payment_service import PaymentService
from model.tools.logger import Logger


class PaymentController:
    @staticmethod
    def edit(id, date_time, amount, description):
        try:
            payment = Payment(id, date_time, amount, description)
            payment.id = id
            PaymentService.edit(payment)
            Logger.info(f"payment edit - {payment}")
            return True, payment
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def save(date_time, amount, description):
        try:
            payment = Payment(date_time, amount, description)
            payment.id = id
            PaymentService.save(payment)
            Logger.info(f"payment save - {payment}")
            return True, payment
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def remove(id):
        try:
            payment = PaymentService.remove(id)
            Logger.info(f"payment remove - {payment}")
        except Exception as e:
            Logger.error(f"{e}")

    @staticmethod
    def findAll():
        try:
            payment_list = PaymentService.find_all()
            Logger.info(f"payment findAll")
            return True, payment_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_id(id):
        try:
            payment = PaymentService.find_by_id()
            Logger.info(f"payment find by id({id})")
            return True, payment
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_amount(amount):
        try:
            payment_list = PaymentService.find_by_amount(amount)
            Logger.info(f"payment find by amount({amount})")
            return True, payment_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_date_time(date_time):
        try:
            payment = PaymentService.find_by_date_time(date_time)
            Logger.info(f"payment by date_time({date_time})")
            return True, payment
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"
