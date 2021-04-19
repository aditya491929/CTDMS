from tkinter import *
import admin
import os

r = Tk(className=" CTDMS Create Tournament")
r.geometry("1530x790")
img = PhotoImage(file='resources\\createTournament.png')
createTournamentPg = Label(r, image=img)
createTournamentPg.pack()

tName = StringVar()
tId = IntVar()
startDate = StringVar()
year = StringVar()
host = StringVar()
prize = StringVar()
numMatches = StringVar()

def back():
    pathstr = os.getcwd()
    pathstr +="\\frontend\\admin.py"
    print(pathstr)
    os.system(pathstr)
    r.destroy()

adminIdEntry = Entry(font=('Yu Gothic', 22), background='#d9d9d9', relief='flat', state='disabled')
adminIdEntry.place(x=680, y=240, width=250)

tourNameEntry = Entry(font=('Yu Gothic', 22),textvariable=tName, background='#d9d9d9', relief='flat')
tourNameEntry.place(x=400, y=330, width=250)

tourIdEntry = Entry(font=('Yu Gothic', 22),textvariable=tId, background='#d9d9d9', relief='flat')
tourIdEntry.place(x=1070, y=330, width=250)

startDateEntry = Entry(font=('Yu Gothic', 22),textvariable=startDate, background='#d9d9d9', relief='flat')
startDateEntry.place(x=400, y=427, width=250)

yearEntry = Entry(font=('Yu Gothic', 22),textvariable=year, background='#d9d9d9', relief='flat')
yearEntry.place(x=1070, y=427, width=250)

hostEntry = Entry(font=('Yu Gothic', 22),textvariable=host, background='#d9d9d9', relief='flat')
hostEntry.place(x=400, y=527, width=250)

prizeEntry = Entry(font=('Yu Gothic', 22),textvariable=prize, background='#d9d9d9', relief='flat')
prizeEntry.place(x=1070, y=527, width=250)

numMatchesEntry = Entry(font=('Yu Gothic', 20),textvariable=numMatches, background='#d9d9d9', relief='flat')
numMatchesEntry.place(x=700, y=618, width=250)

tourBackBtn = Button(width=15, background='#96ddf8', relief='flat', text='Back', font=('Yu Gothic', 18, 'bold'), command=back)
tourBackBtn.place(x=900, y=695)

tourSaveBtn = Button(width=15, background='#7ed957', relief='flat', text='Save', font=('Yu Gothic', 18, 'bold'))
tourSaveBtn.place(x=450, y=695)

r.mainloop()
