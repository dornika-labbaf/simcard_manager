from model.entity.payment import Payment
from model.service.payment_service import PaymentService
from model.tools.decoratoor import exception_handling


class PaymentController:
    @classmethod
    @exception_handling
    def save(cls, date_time, amount, description):
        payment = Payment(date_time, amount, description)
        return True, PaymentService.save(payment)

    @classmethod
    @exception_handling
    def edit(cls, id, date_time, amount, description):
        payment = Payment(id, date_time, amount, description)
        payment.id = id
        return True, PaymentService.edit(payment)

    @classmethod
    @exception_handling
    def remove(cls, id):
        return True, PaymentService.remove(id)

    @classmethod
    @exception_handling
    def findAll(cls):
        return True, PaymentService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, PaymentService.find_by_id()

    @classmethod
    @exception_handling
    def find_by_amount(cls, amount):
        return True, PaymentService.find_by_amount(amount)

    @classmethod
    @exception_handling
    def find_by_date_time(cls, date_time):
        return True, PaymentService.find_by_date_time(date_time)
