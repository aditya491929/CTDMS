from tkinter import *
from tkinter import ttk
from initial import initialize
initialize()
from connect import *


# def main7():
#   r = Tk(className=" CTDMS Add Player")
#   app=AddPlayer(r)

class AddPlayer:
    def back(self):
      self.master.destroy()

    def __init__(self,master):
        self.master=master
        self.master.geometry("1530x790")
        self.img = PhotoImage(file='resources\\addPlayer.png')
        self.addPlayerPg = Label(self.master, image=self.img)
        self.addPlayerPg.pack()

        self.fNameEntry = Entry(self.master,font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
        self.fNameEntry.place(x=470, y=318, width=220)

        self.lNameEntry = Entry(self.master,font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
        self.lNameEntry.place(x=1050, y=318, width=220)

        self.typeSelect = ttk.Combobox(self.master,width=20, font=('Yu Gothic', 15), background="#d9d9d9")
        self.typeSelect['values'] = ('Batsman',
                                'Bowler',
                                'All Rounder'
                                )
        self.typeSelect.place(x=470, y=442)
        self.typeSelect.current()

        self.teamSelect = ttk.Combobox(self.master,width=20, font=('Yu Gothic', 15), background="#d9d9d9")
        self.teamSelect['values'] = ('Batsman',
                                'Bowler',
                                'All Rounder'
                                )
        self.teamSelect.place(x=1050, y=442)
        self.teamSelect.current()

        self.squadSaveBtn = Button(self.master,width=12, background='#ffbcad', relief='flat', text='Save', font=('Yu Gothic', 16, 'bold'),
                            foreground="white")
        self.squadSaveBtn.place(x=707, y=562)

        self.playerInfoBackBtn = Button(self.master,width=15, background='#f4a290', relief='flat', text='Back', font=('Yu Gothic', 18, 'bold'),
                                foreground="white", command=self.back)
        self.playerInfoBackBtn.place(x=100, y=722)

        self.master.mainloop()

# main7()