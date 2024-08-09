from tkinter import ttk

from controller.person_controller import PersonController

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

        self.win = Tk()
        self.win.geometry("800x400")
        self.win.title("person")

        self.id = TextWithLabel(self.win,"id",20,20)
        self.name = TextWithLabel(self.win, "name", 20, 60)
        self.family = TextWithLabel(self.win, "family", 20, 90)
        self.nid = TextWithLabel(self.win, "nid", 20, 110)
        self.date_birth = TextWithLabel(self.win, "date_birth", 20, 140)
        self.father_name = TextWithLabel(self.win, "father_name", 20, 170)
        self.email = TextWithLabel(self.win, "email", 20, 200)
        self.address = TextWithLabel(self.win, "address", 20, 230)





        Button(self.win, text="save", width=10,bg="sky blue", command=self.person_save_click).place(x=20, y=250)
        Button(self.win,text="edit",width=10,bg="seashell2",command=self.person_edit_click).place(x=110,y=250)
        Button(self.win,text="remove",width=10,bg="gold",command=self.person_remove_click).place(x=200,y=250)

        self.table = ttk.Treeview(self.win, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings")

        self.table.column(1, width=60)
        self.table.column(2,width=100)
        self.table.column(3, width=60)
        self.table.column(4, width=100)
        self.table.column(5, width=60)
        self.table.column(6, width=60)
        self.table.column(7, width=60)
        self.table.column(8, width=60)


        self.table.heading(1, text="id")
        self.table.heading(1, text="name")
        self.table.heading(1, text="family")
        self.table.heading(1, text="nid")
        self.table.heading(1, text="date_birth")
        self.table.heading(1, text="father_name")
        self.table.heading(1, text="email")
        self.table.heading(1, text="address")

        self.table.place(x=320,y=20)

        self.reset_form()

        self.win.mainloop()


