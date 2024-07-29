from controller.payment_controller import PaymentController
from model.da.da import DataAccess
from model.entity.payment import Payment
from view.component.table import Table
from view.component.lable_text import TextWithLabel
from tkinter import *
import tkinter.messagebox as msg


class PaymentView:
    def payment_table_click(self, row):
        Payment = self.payment_da.find_by_id(int(row[0]))
        print(Payment)


    def save_click(self):
        status, result = PaymentController.save(self.date_time.get(), self.amount.get(),
                                                self.description.get())
        if status:
            msg.showinfo("PAYMENT SAVE",result)
            self.reset_form()
        elif result.startswith("ERROR"):
            msg.showerror("ERROR",result)



    def edit_click(self):
        status, result = PaymentController.edit(self.date_time.get(), self.amount.get(),
                                                self.description.get())
        if status:
            msg.showinfo("PAYMENT EDIT",result)
            self.reset_form()
        elif result.startswith("ERROR"):
            msg.showerror("ERROR",result)




    def remove_click(self):
        status, result = PaymentController.remove(self.date_time.get(), self.amount.get(),
                                                self.description.get())
        if status:
            msg.showinfo("PAYMENT REMOVE",result)
            self.reset_form()
        elif result.startswith("ERROR"):
            msg.showerror("ERROR",result)



    def __init__(self):
        self.payment_da = DataAccess(Payment)

        self.win = Tk()
        self.win.geometry("800x400")
        self.win.title("payment")

        self.payment_table = Table(self.win,["id","date_time", "amount", "description"],
                             [20,80,60,200],
                             300,20,
                             self.payment_table_click)

        self.total = TextWithLabel(self.win, "date_time:", 20, 20)
        self.total = TextWithLabel(self.win, "amount:", 20, 50)
        self.total = TextWithLabel(self.win, "description:", 20, 80)


        Button(self.win, text="save", width=10,bg="sky blue", command=self.save_click).place(x=20, y=250)
        Button(self.win,text="edit",width=10,bg="seashell2",command=self.edit_click).place(x=110,y=250)
        Button(self.win,text="remove",width=10,bg="gold",command=self.remove_click).place(x=200,y=250)

        self.win.bind()
        self.win.mainloop()
