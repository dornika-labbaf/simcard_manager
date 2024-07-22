from model.da.da import DataAccess
from model.entity import Person
from view.component.table import Table
from view.component.lable_text import TextWithLabel
from tkinter import *

class PersonView:
    def person_table_click(self, row):
        print(row)

    def __init__(self):
        self.person_da = DataAccess(Person)

        self.win = Tk()
        self.geometry("400x400")
        self.win.title("person")

        self.person_table = Table(self.win,["id","name", "family", "nid", "date_birth", "father_name", "email", "address"],
                             [20,60,40,40,40,40,40,50],
                             20,20,
                             self.person_table_click)



        self.win.mainloop()


