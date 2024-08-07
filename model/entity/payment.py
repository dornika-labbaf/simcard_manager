import re
from datetime import datetime
from model.entity.base import Base

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from model.entity import *
from model.tools.validator import *


class Payment(Base):
    __tablename__ = 'payment_tbl'
    _id = Column('id', Integer, primary_key=True, autoincrement=True)
    _date_time = Column('date_time', DateTime, nullable=False)
    _amount = Column('amount', String(20), nullable=False)
    _description = Column('description', String(100))

    _sim_card_id = Column("sim_card_id", ForeignKey("sim_card_tbl.id"))
    sim_card = relationship("SimCard")

    _person_id = Column("person_id",ForeignKey("person_tbl.id"))
    person = relationship("Person")


    def __init__(self, date_time, amount, description):
        self._id = None
        self._date_time = date_time
        self._amount = amount
        self._description = description
        self._sim_card_id = None
        self._person_id = None

    # id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    # date_time
    @property
    def date_time(self):
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        self._date_time = date_time_validator(date_time,"invalid date")

    # amount
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = positive_int_validator(amount, "invalid amount")

    # description
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = name_validator(description,"invalid description")



    @property
    def sim_card_id(self):
        return self._sim_card_id

    @sim_card_id.setter
    def id(self, sim_card_id):
        self._sim_card_id = sim_card_id



    @property
    def person_id(self):
        return self._person_id

    @ person_id.setter
    def id(self,  person_id):
        self. _person_id =  person_id





