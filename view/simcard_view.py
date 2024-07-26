from controller.sim_card_controller import SimCardController
from model.da.da import DataAccess
from model.entity.sim_card import SimCard
from view.component.table import Table
from view.component.lable_text import TextWithLabel
from tkinter import *
import tkinter.messagebox as msg


class SimCardView:
    def simcard_table_click(self, row):
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
        self.simcard.da = DataAccess(SimCard)

        self.win = Tk()
        self.win.geometry("800x400")
        self.win.title("simcard")

        self.simcard_table = Table(self.win,["id","number", "operator", "status", "sim_type", "charge"],
                             [20,60,40,40,40,40],
                             300,20,
                             self.simcard_table_click)



