from tkinter import * 
from tkinter import ttk
from initial import initialize
initialize()
from connect import *

# def main3():
#   r = Tk(className=" CTDMS Create Tournament")
#   app3=CreateTournament(r)

class CreateTournament:
    def addTour(self):
        res = addTournament(self.tourName.get(),self.host.get(),self.year.get(),self.prize.get(),self.startDate.get(),self.adminId)
        if res:
            messagebox.showinfo(" Message","Tournament Created Successfully!")
            self.back()
        else:
            messagebox.showerror("Incomplete Details","All Fields Are Required!")

    def back(self):
        self.master.destroy()

    def __init__(self,master,adminId):
        self.master=master
        self.master.geometry("1530x790")
        self.img = PhotoImage(file='resources\\createTournament.png')
        self.createTournamentPg = Label(self.master, image=self.img)
        self.createTournamentPg.pack()

        self.adminId = adminId
        self.tourName = StringVar()
        self.tourId = StringVar()
        self.startDate = StringVar()
        self.year = StringVar()
        self.host = StringVar()
        self.prize = StringVar()
        self.numMatches = StringVar()

        self.adminIdMessage = Message(self.master,font=('Yu Gothic', 22),text=adminId, background='#d9d9d9', relief='flat')
        self.adminIdMessage.place(x=680, y=240, width=250)

        self.tourNameEntry = Entry(self.master,font=('Yu Gothic', 22), textvariable=self.tourName, background='#d9d9d9', relief='flat')
        self.tourNameEntry.place(x=400, y=330, width=250)

        self.tourIdEntry = Entry(self.master,font=('Yu Gothic', 22), textvariable=self.tourId, background='#d9d9d9', relief='flat')
        self.tourIdEntry.place(x=1070, y=330, width=250)

        self.startDateEntry = Entry(self.master,font=('Yu Gothic', 22), textvariable=self.startDate, background='#d9d9d9', relief='flat')
        self.startDateEntry.place(x=400, y=427, width=250)

        self.yearEntry = Entry(self.master,font=('Yu Gothic', 22), textvariable=self.year, background='#d9d9d9', relief='flat')
        self.yearEntry.place(x=1070, y=427, width=250)

        self.hostEntry = Entry(self.master,font=('Yu Gothic', 22), textvariable=self.host, background='#d9d9d9', relief='flat')
        self.hostEntry.place(x=400, y=527, width=250)

        self.prizeEntry = Entry(self.master,font=('Yu Gothic', 22), textvariable=self.prize, background='#d9d9d9', relief='flat')
        self.prizeEntry.place(x=1070, y=527, width=250)

        self.numMatchesEntry = Entry(self.master,font=('Yu Gothic', 20), textvariable=self.numMatches, background='#d9d9d9', relief='flat')
        self.numMatchesEntry.place(x=700, y=618, width=250)

        self.tourBackBtn = Button(self.master,width=15, background='#96ddf8', relief='flat', text='Back', font=('Yu Gothic', 18, 'bold'), 
                                  command=self.back)
        self.tourBackBtn.place(x=900, y=695)

        self.tourSaveBtn = Button(self.master,width=15, background='#7ed957', relief='flat', text='Save', font=('Yu Gothic', 18, 'bold'),
                                  command=self.addTour)
        self.tourSaveBtn.place(x=450, y=695)

        self.master.mainloop()

# main3()
