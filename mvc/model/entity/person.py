from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from mvc.model.entity.base import Base


class Person(Base):
    _id = Column('id', Integer, primary_key=True, auto_increment=True)
    _name = Column('name', String, nullable=False)
    _family = Column('family', String, nullable=False)
    _nid = Column('nid', Integer, nullable=False)
    _date_birth = Column('date_birth', Integer, nullable=False)

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
