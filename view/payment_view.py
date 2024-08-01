from controller.payment_controller import PaymentController
from model.da.da import DataAccess
from model.entity.payment import Payment
from view.component.table import Table
from view.component.lable_text import TextWithLabel
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk


class PaymentView:
    def reset_form(self):
        self.table.delete(*self.table.get_children())
        status, payment_list = PaymentController.findAll()
        if status:
            for payment in payment_list:
                self.table.insert("",END,values=(payment.id,payment.date_time,payment.amount,payment.description))



    def save_click(self):
        status, result = PaymentController.save(self.date_time.variable.get(), self.amount.variable.get(),
                                                self.description.variable.get())
        if status:
            msg.showinfo("PAYMENT SAVE",result)
            self.reset_form()
        elif result.startswith("ERROR"):
            msg.showerror("ERROR",result)



    def edit_click(self):
        status, result = PaymentController.edit(self.date_time.variable.get(), self.amount.variable.get(),
                                                self.description.variable.get())
        if status:
            msg.showinfo("PAYMENT EDIT",result)
            self.reset_form()
        elif result.startswith("ERROR"):
            msg.showerror("ERROR",result)




    def remove_click(self):
        status, result = PaymentController.remove(self.date_time.variable.get(), self.amount.variable.get(),
                                                self.description.variable.get())
        if status:
            msg.showinfo("PAYMENT REMOVE",result)
            self.reset_form()
        elif result.startswith("ERROR"):
            msg.showerror("ERROR",result)



    def __init__(self):

        self.win = Tk()
        self.win.geometry("800x400")
        self.win.title("payment")

        self.id = TextWithLabel(self.win, "id",20,20)
        self.date_time = TextWithLabel(self.win,"date time",20,60)
        self.amount = TextWithLabel(self.win,"amount",20,90)
        self.description = TextWithLabel(self.win,"description",20,120)
        self.row_remove = TextWithLabel(self.win, "id for remove",20, 140)

        Button(self.win, text="save", width=10,bg="sky blue", command=self.save_click).place(x=20, y=250)
        Button(self.win,text="edit",width=10,bg="seashell2",command=self.edit_click).place(x=110,y=250)
        Button(self.win,text="remove",width=10,bg="gold",command=self.remove_click).place(x=200,y=250)

        self.table = ttk.Treeview(self.win, columns=(1, 2, 3, 4), show="headings")

        self.table.column(1, width=60)
        self.table.column(2,width=100)
        self.table.column(3, width=60)
        self.table.column(4, width=100)


        self.table.heading(1, text="id")
        self.table.heading(1, text="date time")
        self.table.heading(1, text="amount")
        self.table.heading(1, text="description")

        self.table.place(x=320,y=20)

        self.reset_form()
        self.win.mainloop()
