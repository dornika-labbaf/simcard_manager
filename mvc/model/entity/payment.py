from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from mvc.model.entity.base import Base
from mvc.model.entity.sim_card import SimCard
from mvc.model.entity.person import Person


class Payment(Base):
    _id = Column('id', Integer, primary_key=True, auto_increment=True)
    _date_time=Column('date_time',Integer,nullable=False)
    _amount=Column('amount',String(20),nullable=False)
    _description=Column('description',String(20),nullable=False)

    _sim_card_id = Column("sim_Card_id", ForeignKey("sim_card_tbl.id"))
    sim_card = relationship("SimCard")

    def __init__(self, date_time, amount, description):
        self._id = None
        self._date_time = date_time
        self._amount = amount
        self._description = description

    # date_time
    @property
    def date_time(self):
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        self._date_time = date_time

    # amount
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    # description
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description
