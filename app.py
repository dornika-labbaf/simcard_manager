from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk
from view.payment_view import PaymentView
from view.simcard_view import SimCardView
from view.person_view import PersonView




class FrontView:


    def show_view_person(self):
        msg.showinfo("question","مشخصات فردی خود را وارد کنید")
        ui = PersonView()

    def show_view_sim_card(self):
        ui = SimCardView()


    def show(self):
        self.win = Tk()
        self.win.title("view")
        self.win.geometry("400x400")

        Button(self.win, text="ایجاد حساب",command=self.show_view_person).place(x=20,y=20)
        Button(self.win,text="مشخصات سیم کارت",command=self.show_view_sim_card).place(x=20,y=60)

        self.table = ttk.Treeview(self.win, columns=(1,2),show="headings")

        self.table.place(x=300,y=20)


        self.reset_form()


        self.win.mainloop()


ui = PersonView()
ui.show()

