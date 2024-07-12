import re
from datetime import datetime
from model.entity.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from model.entity import *


class Payment(Base):
    __tablename__ = 'payment_tbl'
    _id = Column('id', Integer, primary_key=True, autoincrement=True)
    _date_time = Column('date_time', DateTime, nullable=False)
    _amount = Column('amount', Integer, nullable=False)
    _description = Column('description', String(20), nullable=False)

    _sim_card_id = Column("sim_Card_id", ForeignKey("sim_card_tbl.id"))
    sim_card = relationship("SimCard")

    def __init__(self, date_time, amount, description):
        self._id = None
        self._date_time = date_time
        self._amount = amount
        self._description = description

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

    # validator

    def date_time_validator(self, date_time):
        if isinstance(date_time, datetime):
            return date_time
        else:
            raise ValueError("invalid date_time")

    def amount_validator(self, amount):
        if isinstance(amount, int) and re.match(r"^\d{10}$", amount):
            return amount
        else:
            raise ValueError("invalid amount")

    def description_validator(self, description):
        if isinstance(description, str) and re.match(r"^[a-zA-Z\s]{20}$", description):
            return description
        else:
            raise ValueError("invalid description")