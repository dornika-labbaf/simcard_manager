from controller.sim_card_controller import SimCardController
from model.da.da import DataAccess
from model.entity.sim_card import SimCard
from view.component.table import Table
from view.component.lable_text import TextWithLabel
from tkinter import *
import tkinter.messagebox as msg


class SimCardView:
    def sim_card_table_click(self, row):
        SimCard = self.simcard_da.find_by_id(int(row[0]))
        print(SimCard)

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
        self.simcard_da = DataAccess(SimCard)

        self.win = Tk()
        self.win.geometry("800x400")
        self.win.title("simcard")

        self.simcard_table = Table(self.win,["id","number", "operator", "status", "sim_type", "charge"],
                             [20,60,60,60,60,60],
                             300,20,
                             self.sim_card_table_click)

        self.total = TextWithLabel(self.win, "number:", 20, 20)
        self.total = TextWithLabel(self.win, "operator:", 20, 50)
        self.total = TextWithLabel(self.win, "status:", 20, 80)
        self.total = TextWithLabel(self.win, "sim_type:", 20, 110)
        self.total = TextWithLabel(self.win, "charge:", 20, 140)

        Button(self.win, text="save", width=10,bg="sky blue", command=self.save_click).place(x=20, y=250)
        Button(self.win,text="edit",width=10,bg="seashell2",command=self.edit_click).place(x=110,y=250)
        Button(self.win,text="remove",width=10,bg="gold",command=self.remove_click).place(x=200,y=250)
        self.win.bind()
        self.win.mainloop()


