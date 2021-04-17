from tkinter import *
from tkinter import ttk

r = Tk(className=" CTDMS Team View")
r.geometry("1530x790")
img = PhotoImage(file='resources\\teamView.png')
teamViewPg = Label(r, image=img)
teamViewPg.pack()

style = ttk.Style()
style.theme_use("vista")
style.configure("upcomingMatches.Treeview.Heading",
                background="#efefef",
                foreground="black",
                rowheight=45,
                fieldbackground="#d3d3d3",
                font=('Yu Gothic', 20, 'bold')
                )
style.configure("upcomingMatches.Treeview",
                background="#d3d3d3",
                foreground="black",
                rowheight=35,
                fieldbackground="#d3d3d3",
                font=('Yu Gothic', 15, 'bold')
                )
# style.layout("upcomingMatches.Treeview",[('table.Treeview.treearea', {'sticky': 'nswe'})]) #remove border
style.map('Treeview', background=[('selected', '#caf6ff')])

upcomingMatches = ttk.Treeview(r, style="upcomingMatches.Treeview")

upcomingMatches['columns'] = ("opponent", "date", "time", "venue")
upcomingMatches['show'] = 'headings'
upcomingMatches.column("opponent", width=180, anchor='center')
upcomingMatches.column("date", width=140, anchor='center')
upcomingMatches.column("time", width=130, anchor='center')
upcomingMatches.column("venue", width=250, anchor='center')

upcomingMatches.heading("opponent", text="Opponent")
upcomingMatches.heading("date", text="Date")
upcomingMatches.heading("time", text="Time")
upcomingMatches.heading("venue", text="Venue")

marginTop = 300
for i in range(5):
    row = Label(width=99, height=3, background="#efefef")
    row.place(x=48, y=marginTop)
    radio = Radiobutton(row)
    radio.place(x=15, y=10)
    opponent = Label(row, width=5, height=1, background="#efefef", text="CSK", font=('Yu Gothic', 14, 'bold'))
    opponent.place(x=50, y=6)
    date = Label(row, width=10, height=1, background="#efefef", text="2020/05/03", font=('Yu Gothic', 14, 'bold'))
    date.place(x=180, y=6)
    time = Label(row, width=10, height=1, background="#efefef", text="14:30", font=('Yu Gothic', 14, 'bold'))
    time.place(x=320, y=6)
    venue = Label(row, width=20, height=1, background="#efefef", text="Chinnasyammy stadium",
                  font=('Yu Gothic', 14, 'bold'))
    venue.place(x=440, y=6)
    marginTop += 60

upcomingMatches.place(x=45, y=250)

style = ttk.Style()
style.theme_use("vista")
style.configure("player.Treeview.Heading",
                background="#efefef",
                foreground="black",
                rowheight=40,
                fieldbackground="#d3d3d3",
                font=('Yu Gothic', 20, 'bold')
                )
style.configure("player.Treeview",
                background="#d3d3d3",
                foreground="black",
                rowheight=31,
                fieldbackground="#d3d3d3",
                font=('Yu Gothic', 15, 'bold')
                )
# style.layout("player.Treeview",[('table.Treeview.treearea', {'sticky': 'nswe'})]) #remove border
style.map('Treeview', background=[('selected', '#caf6ff')])

player = ttk.Treeview(r, style="player.Treeview")

player['columns'] = ("name", "type", "selected")
player['show'] = 'headings'
player.column("name", width=280, anchor='center')
player.column("type", width=230, anchor='center')
player.column("selected", width=130, anchor='center')

player.heading("name", text="Name")
player.heading("type", text="Player Type")
player.heading("selected", text="Selected")


marginTop = 300
for i in range(5):
    row1 = Label(width=90, height=3, background="#efefef")
    row1.place(x=824, y=marginTop)
    name = Label(row1, width=20, height=1, background="#efefef", text="suryakumar yadav", font=('Yu Gothic', 14, 'bold'))
    name.place(x=10, y=6)
    type = Label(row1, width=12, height=1, background="#efefef", text="Batsman", font=('Yu Gothic', 14, 'bold'))
    type.place(x=320, y=6)
    selected = Checkbutton(row1)
    selected.place(x=550, y=8)
    marginTop += 60

player.place(x=820, y=250)

squadSaveBtn = Button(width=12, background='#ffbcad', relief='flat', text='Save', font=('Yu Gothic', 16, 'bold'),
                     foreground="white")
squadSaveBtn.place(x=1267, y=612)

teamBackBtn = Button(width=15, background='#f4a290', relief='flat', text='Back', font=('Yu Gothic', 18, 'bold'),
                     foreground="white")
teamBackBtn.place(x=100, y=722)

ptsTableBtn = Button(width=15, background='#f4a290', relief='flat', text='Points Table', font=('Yu Gothic', 18, 'bold'),
                     foreground="white")
ptsTableBtn.place(x=1260, y=722)
r.mainloop()