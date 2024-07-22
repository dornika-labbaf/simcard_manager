from controller.person_controller import PersonController
from model.da.da import DataAccess
from model.entity import Person
from view.component.table import Table
from view.component.lable_text import TextWithLabel
from tkinter import *

class PersonView:
    def person_table_click(self, row):
        Person = self.person_da.find_by_id(int(row[0]))
        print(Person)

    def person_save_click(self):
       status, result =PersonController.save(self.name.get(),self.family.get(),self.nid.get(),self.date_birth.get(),self.father_name.get(),self.email.get(),self.address.get())

    def __init__(self):
        self.person_da = DataAccess(Person)

        self.win = Tk()
        self.win.geometry("800x400")
        self.win.title("person")

        self.person_table = Table(self.win,["id","name", "family", "nid", "date_birth", "father_name", "email", "address"],
                             [20,60,40,40,40,40,40,50],
                             300,20,
                             self.person_table_click)

        self.total = TextWithLabel(self.win, "name:", 20, 20)
        self.total = TextWithLabel(self.win, "family:", 20, 50)
        self.total = TextWithLabel(self.win, "nid:", 20, 80)
        self.total = TextWithLabel(self.win, "birth date:", 20, 110)
        self.total = TextWithLabel(self.win, "father name:", 20, 140)
        self.total = TextWithLabel(self.win, "email:", 20, 170)
        self.total = TextWithLabel(self.win, "address:", 20, 200)

        Button(self.win, text='sell', width=10, command=self.person_save_click).place(x=20, y=250)

        self.win.bind()
        self.win.mainloop()


