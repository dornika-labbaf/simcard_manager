from model.da.da import DataAccess
from model.entity import Person, SimCard, Payment
from view.component.table import Table
from view.component.lable_text import TextWithLabel
from tkinter import *

class SimCardView:
    def person_table_click(self,row):
        Person = self.person_da.find_by_id(int(row[0]))
        print(Person)

    def sim_card_table_click(self,row):
        print(row)

    def payment_table_click(self,row):
        print(row)


    def __init__(self):
        self.person_da = DataAccess(Person)
        self.sim_card_da = DataAccess(SimCard)
        self.payment_da = DataAccess(Payment)


        self.win = Tk()
        self.win.geometry("900x400")
        self.win.title("Simcard manager")


        self.person_table = Table(self.win,["id","name", "family", "nid", "date_birth", "father_name", "email", "address"],
                             [20,60,40,40,40,40,40,50],
                             20,20,
                             self.person_table_click)

        self.person_table.refresh_table(self.person_da.find_all())

        self.sim_card_table = Table(self.win,["id","number","operator","status","sim_type","charge"],
                               [20,60,50,50,60,60],
                               380,20,
                               self.sim_card_table_click)

        # self.sim_card_table.refresh_table(self.sim_card_da.find_all())

        self.payment_table = Table(self.win,["id","date_time", "amount", "description"],
                              [20,60,50,70],
                              700,20,
                              self.payment_table_click)

        #self.payment_table.refresh_table(self.payment_da.find_all())


        self.total = TextWithLabel(self.win,"total", 400,350)


        self.win.mainloop()

