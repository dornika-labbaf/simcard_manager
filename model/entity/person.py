import re
from model.entity.base import Base
from sqlalchemy import Column, Integer, String, Date
from model.entity import *
from model.tools.validator import pattern_validator

class Person(Base):
    __tablename__ = 'person_tbl'
    _id = Column('id', Integer, primary_key=True, autoincrement=True)
    _name = Column('name', String(20), nullable=False)
    _family = Column('family', String(20), nullable=False)
    _nid = Column('nid', String(20), nullable=False)
    _date_birth = Column('date_birth', Date, nullable=False)
    _father_name = Column('father_name', String(20), nullable=False)
    _email = Column('email', String(20), nullable=False)
    _address = Column('address', String(20), nullable=False)

    def __init__(self, name, family, nid, date_birth, father_name, email, address):
        self._id = None
        self._name = name
        self._family = family
        self._nid = nid
        self._date_birth = date_birth
        self._father_name = father_name
        self._email = email
        self._address = address

    # id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    # name
    @property
    def name(self):
        return self._name

    @name.setter
    @pattern_validator(r"^[a-zA-Z]{3,20}$","invallid name")
    def name(self, name):
        self._name = name

    # nid
    @property
    def nid(self):
        return self._nid

    @nid.setter
    def nid(self, nid):
        self._nid = nid

    # date_birth
    @property
    def date_birth(self):
        return self._date_birth

    @date_birth.setter
    def date_birth(self, date_birth):
        self._date_birth = date_birth

    # family
    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = family

    # father_name
    @property
    def father_name(self):
        return self._father_name

    @father_name.setter
    def father_name(self, father_name):
        self._father_name = father_name

    # email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    # address
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address
