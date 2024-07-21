import re
from datetime import date, datetime


def pattern_validator(pattern, message):
    def inner1(function_name):
        def inner2(self, text):
            if isinstance(text,str) and re.match(pattern, text):
                result = function_name(self, text)
            else:
                raise ValueError(message)
            return result
        return inner2
    return inner1


def date_validator(message):
    def inner1(function_name):
        def inner2(self, date_param):
            if isinstance(date_param, date):
                result = function_name(self, date_param)
            elif isinstance(date_param, str):
                date_param = date_param.replace('/', '-')
                try:
                    date_param = datetime.strptime(date_param, '%Y-%m-%d').date()
                    result = function_name(self, date_param)
                except:
                    raise ValueError(message)
            else:
                raise ValueError(message)
            return result
        return inner2
    return inner1


def date_time_validator(message):
    def inner1(function_name):
        def inner2(self, date_time_param):
            if isinstance(date_time_param, date):
                result = function_name(self, date_time_param)
            elif isinstance(date_time_param, str):
                date_time_param = date_time_param.replace('/', '-')
                try:
                    date_time_param = datetime.strptime(date_time_param, '%Y-%m-%d %H:%M:%S').date()
                    result = function_name(self, date_time_param)
                except:
                    raise ValueError(message)
            else:
                raise ValueError(message)
            return result
        return inner2
    return inner1


def boolean_validator(message):
    def inner1(function_name):
        def inner2(self, bool_param):
            if isinstance(bool_param, bool):
                result = function_name(self, bool_param)
            else:
                raise ValueError(message)
            return result

        return inner2

    return inner1


class Validator:
    #payment

    def date_time_validator(self, date_time):
        if isinstance(date_time, datetime):
            return date_time
        else:
            raise ValueError("invalid date_time")

    def amount_validator(self, amount):
        if isinstance(amount, str) and re.match(r"^\d{10}$", amount):
            return amount
        else:
            raise ValueError("invalid amount")

    def description_validator(self, description):
        if isinstance(description, str) and re.match(r"^[a-zA-Z\s]{20}$", description):
            return description
        else:
            raise ValueError("invalid description")

    #person

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
        if isinstance(date_birth, date):
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

    #simcard

    def number_validator(self, number):
        if isinstance(number, str) and re.match(r"^(?:\+98|0)?9\d{9}$", number):
            return number
        else:
            raise ValueError("invalid number")

    def operator_validator(self, operator):
        if isinstance(operator, str) and re.match(r"^(Irancel|hamrah aval|rightel|shatel)$", operator, re.I):
            return operator
        else:
            raise ValueError("invalid operator")

    def status_validator(self, status):
        if isinstance(status, str) and re.match(r"^[a-zA-Z\s]{1,20}$", status):
            return status
        else:
            raise ValueError("invalid status")

    def sim_type_validator(self, sim_type):
        if isinstance(sim_type, str) and re.match(r"^[a-zA-Z\s]{1,20}$", sim_type):
            return sim_type
        else:
            raise ValueError("invalid sim_type")

    def charge_validator(self, charge):
        if isinstance(charge, str) and re.match(r"^\d{1,20}$", charge):
            return charge
        else:
            raise ValueError("invalid charge")




