import re

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model.entity import *
from model.entity.base import Base


class SimCard(Base):
    __tablename__ = 'sim_card_tbl'

    _id = Column('id', Integer, primary_key=True, autoincrement=True)
    _number = Column('number', String(20), nullable=False)
    _operator = Column('operator', String(20), nullable=False)
    _status = Column('status', String(20), nullable=False)
    _sim_type = Column('sim_type', String(20), nullable=False)
    _charge = Column('charge', String(20), nullable=False)

    #_owner_id = Column("owner_id", Integer, ForeignKey("person_tbl.id"))
    #owner = relationship("Person")

    def __init__(self, number, operator, status, sim_type, charge):
        self._id = None
        self._number = number
        self._operator = operator
        self._status = status
        self._sim_type = sim_type
        self._charge = charge

    # id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    # number
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    # oparator
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, operator):
        self._operator = operator

    # status
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    # type
    @property
    def sim_type(self):
        return self._sim_type

    @sim_type.setter
    def sim_type(self, sim_type):
        self._sim_type = sim_type

    # charge
    @property
    def charge(self):
        return self._charge

    @charge.setter
    def charge(self, charge):
        self._charge = charge

    # validator

    def number_validator(self, number):
        if isinstance(number, str) and re.match(r"^[+98|09]\d{11}$", number):
            return number
        else:
            raise ValueError("invalid number")

    def operator_validator(self, operator):
        if isinstance(operator, str) and re.match(r"^[Irancel|hamrah aval|rightel|shatel\s]$", operator):
            return operator
        else:
            raise ValueError("invalid operator")

    def status_validator(self, status):
        if isinstance(status, str) and re.match(r"^[a-zA-Z\s]{20}$", status):
            return status
        else:
            raise ValueError("invalid status")

    def sim_type_validator(self, sim_type):
        if isinstance(sim_type, str) and re.match(r"^[a-zA-Z\s]{20}$", sim_type):
            return sim_type
        else:
            raise ValueError("invalid sim_type")

    def charge_validator(self, charge):
        if isinstance(charge, str) and re.match(r"^[\d]{20}$", charge):
            return charge
        else:
            raise ValueError("invalid charge")
