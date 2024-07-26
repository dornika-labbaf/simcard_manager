from controller.payment_controller import PaymentController
from model.da.da import DataAccess
from model.entity.payment import Payment
from view.component.table import Table
from view.component.lable_text import TextWithLabel
from tkinter import *
import tkinter.messagebox as msg


class PaymentView:
    def payment_table_click(self,row):
        Payment = self.payment_table_click(int(row[0]))
        print(Payment)


    def save_click(self):
        status, result = PaymentController.save(self.date_time.variable.get(), self.amount.variable.get(),
                                                self.description.variable.get())
        if status:
            msg.showinfo("PAYMENT SAVE",result)
            self.reset_form()
        elif result.startswith("ERROR"):
            msg.showerror("ERROR",result)

