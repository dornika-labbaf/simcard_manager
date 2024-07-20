import re
from model.entity.base import Base
from sqlalchemy import Column, Integer, String, Date
from model.entity import *


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

    def name_validator(self, name):
        if isinstance(name, str) and re.match(r"^[a-zA-Z\s]{20}$", name):
            return name
        else:
            raise ValueError("invalid name")

    def nid_validator(self, nid):
        if isinstance(nid, str) and re.match(r"^[\d]{10}$", nid):
            return nid
        else:
            raise ValueError("invalid nid")

    def family_validator(self, family):
        if isinstance(family, str) and re.match(r"^[a-zA-Z\s]{20}$", family):
            return family
        else:
            raise ValueError("invalid family")

    def date_birth_validator(self, date_birth):
        if isinstance(date_birth, Date):
            return date_birth
        else:
            raise ValueError("invalid date_birth")

    def father_name_validator(self, father_name):
        if isinstance(father_name, str) and re.match(r"^[a-zA-Z\s]{20}$", father_name):
            return father_name
        else:
            raise ValueError("invalid father_name")

    def email_validator(self, email):
        if isinstance(email, str) and re.match(r"^@\w(yahoo|gmail).com$", email, re.I):
            return email
        else:
            raise ValueError("invalid email")

    def address_validator(self, address):
        if isinstance(address, str) and re.match(r"^[\w\s]{20}$", address, re.I):
            return address
        else:
            raise ValueError("invalid address")

