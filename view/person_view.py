from controller.person_controller import PersonController
from model.da.da import DataAccess
from model.entity.person import Person
from view.component.table import Table
from view.component.lable_text import TextWithLabel
from tkinter import *
import tkinter.messagebox as msg

class PersonView:
    def reset_form(self):
        self.table.delete(*self.table.get_children())
        status, person_list = PersonController.findAll()
        if status:
            for person in person_list:
                self.table.insert("",END,values=(person.id,person.name,person.family,person.nid,person.date_birth,person.father_name,person.email,person.address))


    def person_save_click(self):
       status, result =PersonController.save(self.name.variable.get(),self.family.variable.get(),self.nid.variable.get(),
                                             self.date_birth.variable.get(),self.father_name.variable.get(),self.email.variable.get(),
                                             self.address.variable.get())
       if status:
           msg.showinfo("PERSON SAVED!",result)
           self.reset_form()
       elif result.startswith("ERROR"):
           msg.showerror("ERROR",result)

    def person_edit_click(self):
        status, result = PersonController.edit(self.name.variable.get(), self.family.variable.get(), self.nid.variable.get(),
                                               self.date_birth.variable.get(), self.father_name.variable.get(), self.email.variable.get(),
                                               self.address.variable.get())
        if status:
            msg.showinfo("PERSON EDITED",result)
            self.reset_form()
        elif result.startswith("ERROR"):
            msg.showerror("ERROR",result)



    def person_remove_click(self):
        status, result = PersonController.save(self.name.variable.get(), self.family.variable.get(), self.nid.variable.get(),
                                               self.date_birth.variable.get(), self.father_name.variable.get(), self.email.variable.get(),
                                               self.address.variable.get())
        if status:
            msg.showinfo("PERSON REMOVE",result)
            self.reset_form()
        elif result.startswith("ERROR"):
            msg.showerror("ERROR",result)





    def __init__(self):
        self.person_da = DataAccess(Person)

        self.win = Tk()
        self.win.geometry("800x400")
        self.win.title("person")

        self.person_table = Table(self.win,["id","name", "family", "nid", "date_birth", "father_name", "email", "address"],
                             [20,60,40,40,40,40,40,50],
                             300,20,
                             self.reset_form)

        self.total = TextWithLabel(self.win, "name:", 20, 20)
        self.total = TextWithLabel(self.win, "family:", 20, 50)
        self.total = TextWithLabel(self.win, "nid:", 20, 80)
        self.total = TextWithLabel(self.win, "birth date:", 20, 110)
        self.total = TextWithLabel(self.win, "father name:", 20, 140)
        self.total = TextWithLabel(self.win, "email:", 20, 170)
        self.total = TextWithLabel(self.win, "address:", 20, 200)

        Button(self.win, text="save", width=10,bg="sky blue", command=self.person_save_click).place(x=20, y=250)
        Button(self.win,text="edit",width=10,bg="seashell2",command=self.person_edit_click).place(x=110,y=250)
        Button(self.win,text="remove",width=10,bg="gold",command=self.person_remove_click).place(x=200,y=250)

        self.win.bind()
        self.win.mainloop()


