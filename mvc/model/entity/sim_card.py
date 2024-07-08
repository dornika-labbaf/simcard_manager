from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from mvc.model.entity.base import Base


class SimCard(Base):
    __tablenames__ = "sim_card_tb;"

    _id = Column('id', Integer, primary_key=True, auto_increment=True)
    _number = Column('number', String(20), nullable=False)
    _operator = Column('operator', String(20), nullable=False)
    _status = Column('status', String(20), nullable=False)
    _type = Column('type', String(20), nullable=False)
    _charge = Column('charge', String(20), nullable=False)

    _owner_id = Column("owner_id", Integer, ForeignKey("person_tbl.id"))
    owner = relationship("Person")

    def __init__(self, name, number, operator, status, type, charge):
        self._id = None
        self._number = number
        self._operator = operator
        self._status = status
        self._type = type
        self._charge = charge

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
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    # charge
    @property
    def charge(self):
        return self._charge

    @charge.setter
    def charge(self, charge):
        self._charge = charge
