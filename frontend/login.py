from tkinter import Tk,PhotoImage,Entry,Button,Label

r = Tk(className=" Cricket Tournament Management System")
r.geometry("1530x790")
img = PhotoImage(file='resources\login.png')
loginPg = Label(r, image=img)
loginPg.pack()

adminUser = Entry(font=('Yu Gothic', 20), background='#ebebeb', relief='flat')
adminUser.place(x=220, y=403)
adminPass = Entry(font=('Yu Gothic', 20), background='#ebebeb', relief='flat', show='*')
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
r.mainloop()
