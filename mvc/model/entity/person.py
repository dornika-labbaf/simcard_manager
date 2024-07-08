import re

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship

from mvc.model.entity.base import Base


class Person(Base):
    _id = Column('id', Integer, primary_key=True, auto_increment=True)
    _name = Column('name', String(20), nullable=False)
    _family = Column('family', String(20), nullable=False)
    _nid = Column('nid', String(20), nullable=False)
    _date_birth = Column('date_birth', Date, nullable=False)

    def __init__(self, name, family, nid, date_birth):
        self._id = id
        self._name = name
        self._family = family
        self._nid = nid
        self._date_birth = date_birth

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
