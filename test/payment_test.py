from datetime import datetime
from controller.payment_controller import PaymentController
from model.da.da import DataAccess
from model.entity import Payment

d = datetime(2020, 5, 1,20,18,20)

#payment = Payment(d,200000,"sim card")
#payment_da = DataAccess(Payment)
#payment_da.save(payment)
#print(payment)
PaymentController.save(d,20000,"ffasadhd")