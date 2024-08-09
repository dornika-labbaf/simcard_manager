from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk
from view.payment_view import PaymentView
from view.simcard_view import SimCardView
from view.person_view import PersonView




class FrontView:


    def show_view_person(self):

        ui = PersonView()
        ui.show()

    def show_view_sim_card(self):
        ui = SimCardView()
        ui.show()

    def show_view_payment(self):
        ui = PaymentView()
        ui.show()


    def show(self):
        self.win = Tk()
        self.win.title("مدیریت سیمکارت")
        self.win.geometry("400x400")

        frame1 = Frame(self.win, bd=2, relief="ridge")
        frame1.place(x=10, y=60, width=300, height=180)



        Label(frame1, text="مشخصات فردی خود را وارد کنید")
        Button(frame1, text="  ثبت مشخصات فردی ",command=self.show_view_person,bg="light cyan").place(x=20,y=20)
        Button(frame1,text="ثبت سیم کارت",command=self.show_view_sim_card,bg="honeydew2").place(x=20,y=60)
        Button(frame1, text="ثبت فروش", command=self.show_view_payment,bg="azure2").place(x=20, y=100)


        self.win.mainloop()


ui = FrontView()
ui.show()

