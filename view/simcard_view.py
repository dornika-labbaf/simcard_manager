from tkinter import ttk

from controller.sim_card_controller import SimCardController
from view.component.lable_text import TextWithLabel
from tkinter import *
import tkinter.messagebox as msg


class SimCardView:
    def reset_form(self):
        self.table.delete(*self.table.get_children())
        status, sim_card_list =SimCardController.findAll()
        if status:
            for sim_card in sim_card_list:
                self.table.insert("",END,values=(sim_card.id,sim_card.number,sim_card.operator,sim_card.status,sim_card.sim_type,sim_card.charge))



    def save_click(self):
        status , result =SimCardController.save(self.number.variable.get(),self.operator.variable.get(),
                                                self.status.variable.get(),self.sim_type.variable.get(),
                                                self.charge.variable.get())
        if status:
            msg.showinfo("SIMCARD SAVED!", result)
            self.reset_form()
        elif result.startswith("ERROR"):
            msg.showerror("ERROR", result)


    def edit_click(self):
        status , result =SimCardController.edit(self.number.variable.get(),self.operator.variable.get(),
                                                self.status.variable.get(),self.sim_type.variable.get(),
                                                self.charge.variable.get())
        if status:
            msg.showinfo("SIMCARD EDIT!", result)
            self.reset_form()
        elif result.startswith("ERROR"):
            msg.showerror("ERROR", result)



    def remove_click(self):
        status , result =SimCardController.remove(self.number.variable.get(),self.operator.variable.get(),
                                                self.status.variable.get(),self.sim_type.variable.get(),
                                                self.charge.variable.get())
        if status:
            msg.showinfo("SIMCARD REMOVE!", result)
            self.reset_form()
        elif result.startswith("ERROR"):
            msg.showerror("ERROR", result)




    def __init__(self):
        self.win = Tk()
        self.win.geometry("800x400")
        self.win.title("simcard")

        self.id = TextWithLabel(self.win, "id", 20, 20)
        self.number = TextWithLabel(self.win, "number:", 20, 50)
        self.operator = TextWithLabel(self.win, "operator:", 20, 80)
        self.status = TextWithLabel(self.win, "status:", 20, 110)
        self.sim_type = TextWithLabel(self.win, "sim_type:", 20, 140)
        self.charge = TextWithLabel(self.win, "charge:", 20, 170)

        Button(self.win, text="save", width=10,bg="sky blue", command=self.save_click).place(x=20, y=250)
        Button(self.win,text="edit",width=10,bg="seashell2",command=self.edit_click).place(x=110,y=250)
        Button(self.win,text="remove",width=10,bg="gold",command=self.remove_click).place(x=200,y=250)

        self.table = ttk.Treeview(self.win, columns=(1, 2, 3, 4, 5, 6), show="headings")

        self.table.column(1, width=60)
        self.table.column(2,width=100)
        self.table.column(3, width=60)
        self.table.column(4, width=100)
        self.table.column(5, width=60)
        self.table.column(6, width=60)


        self.table.heading(1, text="id")
        self.table.heading(1, text="number")
        self.table.heading(1, text="operator")
        self.table.heading(1, text="status")
        self.table.heading(1, text="sim_type")
        self.table.heading(1, text="charge")

        self.table.place(x=320, y=20)

        self.reset_form()
        self.win.mainloop()


