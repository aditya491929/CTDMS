from tkinter import Tk,PhotoImage,Entry,Button,Label

r = Tk(className="Cricket Tournament Management System")
r.geometry("1520x790")
img = PhotoImage(file='resources/login.png')
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

loginBtnAdmin = Button(width=28, height=2, background='#caf6ff', relief='flat', text='Login',
                       font=('Yu Gothic', 10, 'bold'))
loginBtnAdmin.place(x=317, y=588)

loginBtnTeam = Button(width=28, height=2, background='#caf6ff', relief='flat', text='Login',
                      font=('Yu Gothic', 10, 'bold'))
loginBtnTeam.place(x=958, y=588)
r.mainloop()
