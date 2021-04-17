from tkinter import *
from tkinter import ttk

r = Tk(className=" CTDMS Add Player")
r.geometry("1530x790")
img = PhotoImage(file='resources\\addPlayer.png')
addPlayerPg = Label(r, image=img)
addPlayerPg.pack()

fNameEntry = Entry(font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
fNameEntry.place(x=470, y=318, width=220)

lNameEntry = Entry(font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
lNameEntry.place(x=1050, y=318, width=220)

typeSelect = ttk.Combobox(width=20, font=('Yu Gothic', 15), background="#d9d9d9")
typeSelect['values'] = ('Batsman',
                        'Bowler',
                        'All Rounder'
                        )
typeSelect.place(x=470, y=442)
typeSelect.current()

teamSelect = ttk.Combobox(width=20, font=('Yu Gothic', 15), background="#d9d9d9")
teamSelect['values'] = ('Batsman',
                        'Bowler',
                        'All Rounder'
                        )
teamSelect.place(x=1050, y=442)
teamSelect.current()

squadSaveBtn = Button(width=12, background='#ffbcad', relief='flat', text='Save', font=('Yu Gothic', 16, 'bold'),
                      foreground="white")
squadSaveBtn.place(x=707, y=562)

playerInfoBackBtn = Button(width=15, background='#f4a290', relief='flat', text='Back', font=('Yu Gothic', 18, 'bold'),
                           foreground="white")
playerInfoBackBtn.place(x=100, y=722)

ptsTableBtn = Button(width=15, background='#f4a290', relief='flat', text='Points Table', font=('Yu Gothic', 18, 'bold'),
                     foreground="white")
ptsTableBtn.place(x=1260, y=722)
r.mainloop()