from tkinter import PhotoImage, Entry, Button, Label, messagebox
from tkinter import *
from tkinter import ttk
from initial import initialize
initialize()
from connect import *


# def main7():
#   r = Tk(className=" CTDMS Add Player")
#   app=AddPlayer(r)

class AddPlayer:
    def runSave(self):
        type = self.playerType[self.typeSelect.current()]
        result = addPlayerToTeam(
            self.team_id, self.fname.get(), self.lname.get(), type, "")
        if result:
            messagebox.showinfo(" Message", "Player Added Successfully!")
            self.back()
        else:
            messagebox.showerror(" Incomplete Details",
                                 "Fill Form Completely!")
            self.back()

    def back(self):
        self.master.destroy()

    def __init__(self, master, t_id):
        self.master = master
        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        self.master.geometry("%dx%d+0+0" % (self.width, self.height))
        self.master.state('zoomed')

        self.img = PhotoImage(file='resources\\addPlayer.png')
        self.addPlayerPg = Label(self.master, image=self.img)
        self.addPlayerPg.pack()

        self.team_id = t_id
        self.fname = StringVar()
        self.lname = StringVar()
        self.type = StringVar()

        self.fNameEntry = Entry(self.master, font=(
            'Yu Gothic', 20), textvariable=self.fname, background='#d9d9d9', relief='flat')
        self.fNameEntry.place(x=470, y=318, width=220)

        self.lNameEntry = Entry(self.master, font=(
            'Yu Gothic', 20), textvariable=self.lname, background='#d9d9d9', relief='flat')
        self.lNameEntry.place(x=1050, y=318, width=220)
        self.playerType = ('Batsman', 'Bowler', 'All Rounder')
        self.typeSelect = ttk.Combobox(self.master, width=20, font=(
            'Yu Gothic', 15), background="#d9d9d9")
        self.typeSelect['values'] = self.playerType
        self.typeSelect.place(x=470, y=442)
        self.typeSelect.current()
        teamMap = getTeamNameMapping()
        self.teamSelect = Message(self.master, width=60, font=(
            'Yu Gothic', 15), background="#d9d9d9")
        print(teamMap, teamMap[int(self.team_id)])
        self.teamSelect.config(text=teamMap[int(self.team_id)])
        self.teamSelect.place(x=1050, y=442)

        self.squadSaveBtn = Button(self.master, width=12, background='#ffbcad', relief='flat', text='Save', font=('Yu Gothic', 16, 'bold'),
                                   foreground="white", command=self.runSave)
        self.squadSaveBtn.place(x=707, y=562)

        self.playerInfoBackBtn = Button(self.master, width=15, background='#f4a290', relief='flat', text='Back', font=('Yu Gothic', 18, 'bold'),
                                        foreground="white", command=self.back)
        self.playerInfoBackBtn.place(x=100, y=722)

        self.master.mainloop()

# main7()
