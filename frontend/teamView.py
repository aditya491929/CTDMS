from tkinter import *
from tkinter import ttk

r = Tk(className=" CTDMS Team View")
r.geometry("1530x790")
img = PhotoImage(file='resources\\teamView.png')
teamViewPg = Label(r, image=img)
teamViewPg.pack()

msg = "11"
t_id = Message(r, text=msg, background="#ffbcad", font=('Yu Gothic', 20, 'bold'),foreground="white")
t_id.place(x=980, y=610, width=22)

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

container = ttk.Frame(r)
canvas = Canvas(container, width=700, bg="white")
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all"),
        height=333
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set, background="grey")


for i in range(10):
    row = Label(scrollable_frame,width=99, height=3, background="#d9d9d9")
    row.pack(pady=3)
    radio = Radiobutton(row, background="#d9d9d9")
    radio.place(x=15, y=10)
    opponent = Label(row, width=5, height=1, background="#d9d9d9", text="CSK", font=('Yu Gothic', 14, 'bold'))
    opponent.place(x=50, y=6)
    date = Label(row, width=10, height=1, background="#d9d9d9", text="2020/05/03", font=('Yu Gothic', 14, 'bold'))
    date.place(x=180, y=6)
    time = Label(row, width=10, height=1, background="#d9d9d9", text="14:30", font=('Yu Gothic', 14, 'bold'))
    time.place(x=320, y=6)
    venue = Label(row, width=20, height=1, background="#d9d9d9", text="Chinnasyammy stadium",
                  font=('Yu Gothic', 14, 'bold'))
    venue.place(x=440, y=6)
    

container.place(x=46, y=300)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

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

container1 = ttk.Frame(r)
canvas1 = Canvas(container1, width=637, bg="white")
scrollbar1 = ttk.Scrollbar(container1, orient="vertical", command=canvas1.yview)
scrollable_frame1 = ttk.Frame(canvas1)

scrollable_frame1.bind(
    "<Configure>",
    lambda e1: canvas1.configure(
        scrollregion=canvas1.bbox("all"),
        height=293
    )
)

canvas1.create_window((0, 0), window=scrollable_frame1, anchor="nw")

canvas1.configure(yscrollcommand=scrollbar1.set, background="grey")

for i in range(10):
    row1 = Label(scrollable_frame1,width=90, height=3, background="#d9d9d9")
    row1.pack(pady=3)
    name = Label(row1, width=20, height=1, background="#d9d9d9", text="suryakumar yadav", font=('Yu Gothic', 14, 'bold'))
    name.place(x=10, y=6)
    type = Label(row1, width=12, height=1, background="#d9d9d9", text="Batsman", font=('Yu Gothic', 14, 'bold'))
    type.place(x=320, y=6)
    selected = Checkbutton(row1, background="#d9d9d9")
    selected.place(x=550, y=8)

container1.place(x=824, y=300)
canvas1.pack(side="left", fill="both", expand=True)
scrollbar1.pack(side="right", fill="y")



player.place(x=820, y=250)

squadSaveBtn = Button(width=12, background='#ffbcad', relief='flat', text='Save', font=('Yu Gothic', 16, 'bold'),
                     foreground="white")
squadSaveBtn.place(x=1267, y=612)

teamLogoutBtn = Button(width=15, background='#f4a290', relief='flat', text='Logout', font=('Yu Gothic', 18, 'bold'),
                     foreground="white")
teamLogoutBtn.place(x=100, y=722)

addPlayerBtn = Button(width=17, height=1, background='#f4a290', relief='flat', text='Add Player', font=('Yu Gothic', 18, 'bold'),
                     foreground="white")
addPlayerBtn.place(x=660, y=722)

ptsTableBtn = Button(width=15, background='#f4a290', relief='flat', text='Points Table', font=('Yu Gothic', 18, 'bold'),
                     foreground="white")
ptsTableBtn.place(x=1260, y=722)
r.mainloop()