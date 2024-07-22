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


        self.win.mainloop()


