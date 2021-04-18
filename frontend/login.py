from tkinter import Tk,PhotoImage,Entry,Button,Label,messagebox
import tkinter as tk
from initial import initialize
initialize()
from connect import validateAdmin

r = Tk(className=" Cricket Tournament Management System")
r.geometry("1530x790")
adU=tk.StringVar()
adP=tk.StringVar()

def authenticate():
    print(adU.get(),adP.get())
    check=validateAdmin(adU.get(),adP.get())
    if check==2:
        messagebox.showinfo(" Message","Logged In Successfully!")
    elif check==1:
        messagebox.showerror(" Alert","No Admin Found!")
    else:
        messagebox.showerror(" Alert","Invalid Password")
    
    adU.set("")
    adP.set("")

img = PhotoImage(file='resources\\login.png')
loginPg = Label(r, image=img)
loginPg.pack()

adminUser = Entry(font=('Yu Gothic', 20),textvariable=adU, background='#ebebeb', relief='flat')
adminUser.place(x=220, y=403)
adminPass = Entry(font=('Yu Gothic', 20),textvariable=adP, background='#ebebeb', relief='flat', show='*')
adminPass.place(x=220, y=512)

teamUser = Entry(font=('Yu Gothic', 20), background='#ebebeb', relief='flat')
teamUser.place(x=867, y=403)
teamPass = Entry(font=('Yu Gothic', 20), background='#ebebeb', relief='flat', show='*')
teamPass.place(x=867, y=512)

loginBtnAdmin = Button(width=15, height=1, background='#caf6ff', relief='flat', text='Login',
                       font=('Yu Gothic', 13, 'bold'))
loginBtnAdmin.place(x=345, y=590)

loginBtnTeam = Button(width=15, height=1, background='#caf6ff', relief='flat', text='Login',
                      font=('Yu Gothic', 13, 'bold'))
loginBtnTeam.place(x=990, y=590)

print(adminUser.get(),adminPass.get())
# loginBtnAdmin.config(command=validateAdmin(adminUser.get(),adminPass.get()))
loginBtnAdmin.config(command=authenticate)
r.mainloop()
