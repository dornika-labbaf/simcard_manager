from model.entity.payment import Payment
from model.da.da import DataAccess


class PaymentService:
    @classmethod
    def save(cls,payment):
        payment_da = DataAccess(Payment)
        payment_da.save(payment)
        return payment

    @classmethod
    def edit(cls,payment):
        payment_da = DataAccess(Payment)
        payment_da.edit(payment)
        return payment

    @classmethod
    def remove(cls,id):
        payment_da = DataAccess(Payment)
        return payment_da.remove(id)

    @classmethod
    def find_all(cls):
        payment_da = DataAccess(Payment)
        return payment_da.find_all()

    @classmethod
    def find_by_id(cls,id):
        payment_da = DataAccess(Payment)
        return payment_da.find_by_id(id)

    @classmethod
    def find_by(cls,date_time):
        payment_da = DataAccess(Payment)
        return payment_da.find_by(Payment.date_time == date_time)

    @classmethod
    def find_by(cls,amount):
        payment_da = DataAccess(Payment)
        return payment_da.find_by(Payment.amount == amount)
