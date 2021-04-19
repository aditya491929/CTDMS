from tkinter import *
from tkinter import ttk
from initial import initialize
initialize()
from connect import *


def main6():
  r = Tk(className=" CTDMS Match Result")
  app=MatchResult(r)

class MatchResult:
    def __init__(self,master):
        self.master=master
        self.master.geometry("1530x790")
        self.img = PhotoImage(file='resources\\matchResult.png')
        self.matchResultPg = Label(self.master, image=self.img)
        self.matchResultPg.pack()

        self.matchNoEntry = Entry(self.master,font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
        self.matchNoEntry.place(x=330, y=207, width=200)

        self.tossEntry = Entry(self.master,font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
        self.tossEntry.place(x=1106, y=207, width=200)

        self.runs1Entry = Entry(self.master,font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
        self.runs1Entry.place(x=100, y=388, width=200)

        self.overs1Entry = Entry(self.master,font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
        self.overs1Entry.place(x=447, y=388, width=200)

        self.wickets1Entry = Entry(self.master,font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
        self.wickets1Entry.place(x=100, y=513, width=200)

        self.extras1Entry = Entry(self.master,font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
        self.extras1Entry.place(x=447, y=513, width=200)


        self.runs2Entry = Entry(self.master,font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
        self.runs2Entry.place(x=875, y=388, width=200)

        self.overs2Entry = Entry(self.master,font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
        self.overs2Entry.place(x=1225, y=388, width=200)

        self.wickets2Entry = Entry(self.master,font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
        self.wickets2Entry.place(x=875, y=513, width=200)

        self.extras2Entry = Entry(self.master,font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
        self.extras2Entry.place(x=1225, y=513, width=200)


        self.momEntry = Entry(self.master,font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
        self.momEntry.place(x=270, y=633, width=200)

        self.winEntry = Entry(self.master,font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
        self.winEntry.place(x=730, y=633, width=200)

        self.loseEntry = Entry(self.master,font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
        self.loseEntry.place(x=1210, y=633, width=200)

        self.saveBtn = Button(self.master,width=10, background='#7ed957', relief='flat', text='Save', font=('Yu Gothic', 18, 'bold'))
        self.saveBtn.place(x=545, y=708)

        self.backBtn = Button(self.master,width=10, background='#96ddf8', relief='flat', text='Back', font=('Yu Gothic', 18, 'bold'))
        self.backBtn.place(x=845, y=708)
        self.master.mainloop()

main6()