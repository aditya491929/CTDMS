from tkinter import *
from tkinter import ttk

r = Tk(className=" CTDMS Admin View")
r.geometry("1530x790")
img = PhotoImage(file='resources\\admin.png')
adminViewPg = Label(r, image=img)
adminViewPg.pack()

style = ttk.Style()
style.theme_use("vista")
style.configure("tournament.Treeview.Heading",
                background="#efefef",
                foreground="black",
                rowheight=48,
                fieldbackground="#d3d3d3",
                font=('Yu Gothic', 12, 'bold')
                )
style.configure("tournament.Treeview",
                background="#d3d3d3",
                foreground="black",
                rowheight=43,
                fieldbackground="#d3d3d3",
                font=('Yu Gothic', 10, 'bold'))
# style.layout("table.Treeview",[('tournament.Treeview.treearea', {'sticky': 'nswe'})]) #remove border
style.map('Treeview', background=[('selected', '#caf6ff')])

tournaments = ttk.Treeview(r, style="tournament.Treeview")
tournaments['columns'] = ("TournamentId", "TournamentName", "Host", "Year", "NumberOfMatches", "PrizeMoney", "Winner")
tournaments['show'] = 'headings'
tournaments.column("TournamentId", width=90, anchor="center")
tournaments.column("TournamentName", width=250, anchor="center")
tournaments.column("Host", width=170, anchor="center")
tournaments.column("Year", width=100, anchor="center")
tournaments.column("NumberOfMatches", width=150, anchor="center")
tournaments.column("PrizeMoney", width=120, anchor="center")
tournaments.column("Winner", width=180, anchor="center")

tournaments.heading("TournamentId", text="Id")
tournaments.heading("TournamentName", text="Tournament_name")
tournaments.heading("Host", text="Host")
tournaments.heading("Year", text="Year")
tournaments.heading("NumberOfMatches", text="No_of_matches")
tournaments.heading("PrizeMoney", text="Prize_money")
tournaments.heading("Winner", text="Winner")

tournaments.place(x=55, y=250)

newTournamentBtn = Button(width=17, background='#caf6ff', relief='flat', text='Create New Tournament',
                          font=('Yu Gothic', 14, 'bold'), wraplength=150)
newTournamentBtn.place(x=1250, y=295)

label1 = LabelFrame(text="Enter Tournament Id", background="#caf6ff")
label1.place(x=1228, y=430, width=220, height=60)
idEntry = Entry(label1, font=('Yu Gothic', 14, 'bold'))
idEntry.place(x=10, y=0, width=200, height=40)
viewTournamentBtn = Button(width=18, background='#caf6ff', relief='groove', text='View Tournament Matches',
                           font=('Yu Gothic', 14, 'bold'), wraplength=200)
viewTournamentBtn.place(x=1225, y=505)

adminLogoutBtn = Button(width=18, background='#ff5757', relief='flat', text='Logout',
                           font=('Yu Gothic', 14, 'bold'))
adminLogoutBtn.place(x=1225, y=655)

tournaments.insert(parent='', index='end', iid=0, values=("1", "IPL", "BCCI", "2021", "50", "100000", "MI"))

r.mainloop()