from model.da.da import DataAccess
from model.entity import Payment

payment = Payment("6/5/444",200000,"sim card")
payment = DataAccess(Payment)
payment.save(payment)
print(payment)
