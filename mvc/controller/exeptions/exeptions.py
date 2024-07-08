class SimCardNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("sim_card not found")


class PersonNotFoundError(Exception):
    def __init__(self,*args):
        super().__init__("Person not found")


class PaymentNotFoundError(Exception):
    def __init__(self,*args):
        super().__init__("Payment not found")
