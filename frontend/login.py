from tkinter import Tk,PhotoImage,Entry,Button,Label,messagebox,Toplevel
import tkinter as tk
from initial import initialize
initialize()
from connect import validateAdmin,validateTeam
from admin import AdminWindow
from teamView import TeamView

def main():
  r = Tk(className=" Cricket Tournament Management System")
  app=loginWindow(r)
  
class loginWindow:    
    def authenticate(self):
            print("Login:{} ; Pass:{}".format(self.adU.get(),self.adP.get()))
            check=validateAdmin(self.adU.get(),self.adP.get())
            if check==2:
                messagebox.showinfo(" Message","Logged In Successfully!")
                adminuser = self.adU.get()
                self.adU.set("")
                self.adP.set("")
                self.r1=Toplevel(self.master)
                self.app=AdminWindow(self.r1,adminuser)
            elif check==1:
                messagebox.showerror(" Alert","No Admin Found!")
            else:
                messagebox.showerror(" Alert","Invalid Password")
            
            self.adU.set("")
            self.adP.set("")

    def authenticate1(self):
        print("Login:{} ; Pass:{}".format(self.TU.get(),self.TP.get()))
        check=validateTeam(self.TU.get(),self.TP.get())
        if check==2:
            messagebox.showinfo(" Message","Logged In Successfully!")
            playerUser = self.TU.get()
            self.TU.set("")
            self.TP.set("")
            self.r2=Toplevel(self.master)
            self.app2=TeamView(self.r2,playerUser)

        elif check==1:
            messagebox.showerror(" Alert","No Such Team Found!")
        else:
            messagebox.showerror(" Alert","Invalid Password")
        
        self.TU.set("")
        self.TP.set("")

    def __init__(self,master):
        self.master=master
        self.master.geometry("1530x790")

        self.img = PhotoImage(file='resources\\login.png')
        self.loginPg = Label(self.master, image=self.img)
        self.loginPg.pack()

        self.adU=tk.StringVar() #these two variables store the input givent via the entry widget
        self.adP=tk.StringVar()

        self.TU=tk.StringVar() #these two variables store the input givent via the entry widget
        self.TP=tk.StringVar()

        self.adminUser = Entry(self.master,font=('Yu Gothic', 20),textvariable=self.adU, background='#ebebeb', relief='flat')
        self.adminUser.place(x=220, y=403)
        self.adminPass = Entry(self.master,font=('Yu Gothic', 20),textvariable=self.adP, background='#ebebeb', relief='flat', show='*')
        self.adminPass.place(x=220, y=512)

        self.teamUser = Entry(self.master,font=('Yu Gothic', 20),textvariable=self.TU, background='#ebebeb', relief='flat')
        self.teamUser.place(x=867, y=403)
        self.teamPass = Entry(self.master,font=('Yu Gothic', 20),textvariable=self.TP, background='#ebebeb', relief='flat', show='*')
        self.teamPass.place(x=867, y=512)

        self.loginBtnAdmin = Button(self.master,width=15, height=1, background='#caf6ff', relief='flat', text='Login',
                            font=('Yu Gothic', 13, 'bold'))
        self.loginBtnAdmin.place(x=345, y=590)

        self.loginBtnTeam = Button(self.master,width=15, height=1, background='#caf6ff', relief='flat', text='Login',
                            font=('Yu Gothic', 13, 'bold'))
        self.loginBtnTeam.place(x=990, y=590)

        print(self.adU,self.adP)
        # loginBtnAdmin.config(command=validateAdmin(adminUser.get(),adminPass.get()))
        self.loginBtnAdmin.config(command=self.authenticate)
        self.loginBtnTeam.config(command=self.authenticate1)
        self.master.mainloop()

main()
