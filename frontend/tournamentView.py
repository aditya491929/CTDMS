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

matches['columns'] = ("matchId", "date", "time", "venue", "homeTeam", "awayTeam", "result")
matches['show'] = 'headings'
matches.column("matchId", width=130, anchor='center')
matches.column("date", width=130, anchor='center')
matches.column("time", width=130, anchor='center')
matches.column("venue", width=370, anchor='center')
matches.column("homeTeam", width=250, anchor='center')
matches.column("awayTeam", width=250, anchor='center')
matches.column("result", width=160, anchor='center')

matches.heading("matchId", text="Match Id")
matches.heading("date", text="Date")
matches.heading("time", text="Time")
matches.heading("venue", text="Venue")
matches.heading("homeTeam", text="Home Team")
matches.heading("awayTeam", text="Away Team")
matches.heading("result", text="Add Result")


# matches.insert(parent='', index='end', iid=0, values=("1", "2020/09/2", "14:30:30", "Chinnaswammy stadium", "2", "7",
#                                                       "edtBtn"))

topMargin = 290
for i in range(5):
    row = Label(width=202, height=3, background="#ededed")
    row.place(x=61, y=topMargin)
    edtBtn = Button(row, width=10, background='#caf6ff', relief='groove', text='Result', font=('Yu Gothic', 10, 'bold'))
    edtBtn.place(x=1300, y=7)
    m_id = Label(row, width=7, height=1, background="#ededed", text=i, font=('Yu Gothic', 14, 'bold'))
    m_id.place(x=4, y=5)
    date_lbl = Label(row, width=9, height=1, background="#ededed", text="2021/09/01", font=('Yu Gothic', 14, 'bold'))
    date_lbl.place(x=134, y=5)
    time_lbl = Label(row, width=9, height=1, background="#ededed", text="14:30", font=('Yu Gothic', 14, 'bold'))
    time_lbl.place(x=270, y=5)
    venue_lbl = Label(row, width=25, height=1, background="#ededed", text="chinnasyammy stadium",
                      font=('Yu Gothic', 14, 'bold'))
    venue_lbl.place(x=420, y=5)
    homeTeam_lbl = Label(row, width=15, height=1, background="#ededed", text="csk", font=('Yu Gothic', 14, 'bold'))
    homeTeam_lbl.place(x=790, y=5)
    awayTeam_lbl = Label(row, width=15, height=1, background="#ededed", text="Mi", font=('Yu Gothic', 14, 'bold'))
    awayTeam_lbl.place(x=1029, y=5)
    topMargin += 60

matchbackBtn = Button(width=15, background='#caf6ff', relief='flat', text='Back', font=('Yu Gothic', 18, 'bold'))
matchbackBtn.place(x=120, y=720)

ptsTableBtn = Button(width=15, background='#caf6ff', relief='flat', text='Points Table', font=('Yu Gothic', 18, 'bold'))
ptsTableBtn.place(x=1270, y=720)

matches.place(x=60, y=240)
r.mainloop()

