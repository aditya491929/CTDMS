from tkinter import *
from tkinter import ttk

r = Tk(className=" CTDMS Tournament View")
r.geometry("1530x790")
img = PhotoImage(file='resources\\tournamentView.png')
matchTablePg = Label(r, image=img)
matchTablePg.pack()

msg = "Coming from backend"
t_id = Message(r, text=msg, background="white", font=('Yu Gothic', 10, 'bold'))
t_id.place(x=1363, y=182, width=80)

style = ttk.Style()
style.theme_use("vista")
style.configure("matches.Treeview.Heading",
                background="#efefef",
                foreground="black",
                rowheight=45,
                fieldbackground="#d3d3d3",
                font=('Yu Gothic', 20, 'bold')
                )
style.configure("matches.Treeview",
                background="#d3d3d3",
                foreground="black",
                rowheight=38,
                fieldbackground="#d3d3d3",
                font=('Yu Gothic', 15, 'bold')
                )
# style.layout("matches.Treeview",[('table.Treeview.treearea', {'sticky': 'nswe'})]) #remove border
style.map('Treeview', background=[('selected', '#caf6ff')])

matches = ttk.Treeview(r, style="matches.Treeview")

matches['columns'] = ("matchId", "date", "time", "venue", "homeTeam", "awayTeam")
matches['show'] = 'headings'
matches.column("matchId", width=150, anchor='center')
matches.column("date", width=150, anchor='center')
matches.column("time", width=150, anchor='center')
matches.column("venue", width=370, anchor='center')
matches.column("homeTeam", width=300, anchor='center')
matches.column("awayTeam", width=300, anchor='center')

matches.heading("matchId", text="Match Id")
matches.heading("date", text="Date")
matches.heading("time", text="Time")
matches.heading("venue", text="Venue")
matches.heading("homeTeam", text="Home Team")
matches.heading("awayTeam", text="Away Team")

matches.insert(parent='', index='end', iid=0, values=("1", "2020/09/2", "14:30:30", "Chinnaswammy stadium", "2", "7"))

matchbackBtn = Button(width=15, background='#caf6ff', relief='flat', text='Back', font=('Yu Gothic', 18, 'bold'))
matchbackBtn.place(x=120, y=720)

ptsTableBtn = Button(width=15, background='#caf6ff', relief='flat', text='Points Table', font=('Yu Gothic', 18, 'bold'))
ptsTableBtn.place(x=1270, y=720)

matches.place(x=60, y=240)
r.mainloop()
