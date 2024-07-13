from model.entity.payment import Payment
from model.da.da import DataAccess


class PaymentService:
    @staticmethod
    def save(payment):
        payment_da = DataAccess(Payment)
        payment_da.save(payment)
        return payment

    @staticmethod
    def edit(payment):
        payment_da = DataAccess(Payment)
        payment_da.edit(payment)
        return payment

    @staticmethod
    def remove(id):
        payment_da = DataAccess(Payment)
        return payment_da.remove(id)

    @staticmethod
    def find_all():
        payment_da = DataAccess(Payment)
        return payment_da.find_all()

    @staticmethod
    def find_by_id(id):
        payment_da = DataAccess(Payment)
        return payment_da.find_by_id(id)

    @staticmethod
    def find_by(date_time):
        payment_da = DataAccess(Payment)
        return payment_da.find_by(Payment.date_time == date_time)

    @staticmethod
    def find_by(amount):
        payment_da = DataAccess(Payment)
        return payment_da.find_by(Payment.amount == amount)
