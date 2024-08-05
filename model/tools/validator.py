import re
from datetime import datetime, date


def date_time_validator(date_time, message):
    if isinstance(date_time, datetime):
        return date_time
    else:
        raise ValueError(message)



def boolean_validator(bool_value , message):
    if isinstance(bool_value, bool):
        return bool_value
    else:
        raise ValueError(message)


def positive_int_validator(int_validator, message):
    if isinstance(int_validator, int) and int_validator >=0:
        return int_validator
    else:
        raise ValueError(message)



def name_validator(name, message):
    if isinstance(name, str) and re.match(r"^[a-zA-Z\s]{3,100}$", name):
        return name
    else:
        raise ValueError(message)


def nid_validator(nid, message):
    if isinstance(nid, str) and re.match(r"^[\d]{10}$", nid):
        return nid
    else:
        raise ValueError(message)



def date_birth_validator(date_birth, message):
    if isinstance(date_birth, date):
        return date_birth
    else:
        raise ValueError(message)


def email_validator(email, message):
    if isinstance(email, str) and re.match(r"^@\w(yahoo|gmail).com$", email, re.I):
        return email
    else:
        raise ValueError(message)



def number_validator(number, message):
    if isinstance(number, str) and re.match(r"^(?:\+98|0)?9\d{9}$", number):
        return number
    else:
        raise ValueError(message)


def operator_validator(operator, message):
    if isinstance(operator, str) and re.match(r"^(Irancel|hamrah aval|rightel|shatel)$", operator, re.I):
        return operator
    else:
        raise ValueError(message)



def address_validator(address, message):
    if isinstance(address, str) and re.match(r"^(\w\s){20,100}$",address,re.I):
        return address
    else:
        raise ValueError(message)


def sim_type_validator(sim_type, message):
    if isinstance(sim_type, str) and re.match(r"^(permanent|prepaid)$", sim_type, re.I):
        return sim_type
    else:
        raise ValueError(message)





