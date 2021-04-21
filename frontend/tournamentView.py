from tkinter import *
from tkinter import ttk
from initial import initialize
initialize()
from connect import getMatchesForAdmin
from points import PointsTable
from viewResult import ViewResult
from matchResult import MatchResult


# def maintournamentView():
#     r = Tk(className=" CTDMS Tournament View")
#     app = TourView(r)

class TourView:
    def fillResult(self,details):
        self.r5=Toplevel(self.master)
        self.app5=MatchResult(self.r5,details)

    def ptsView(self):
        self.r=Toplevel(self.master)
        self.app=PointsTable(self.r,self.matchList[0][0])

    def back(self):
        self.master.destroy()

    def __init__(self, master, matchesList):
        self.master = master
        self.width=self.master.winfo_screenwidth()
        self.height=self.master.winfo_screenheight()
        self.master.geometry("%dx%d+0+0"%(self.width,self.height))
        self.master.state('zoomed')
        self.img = PhotoImage(file='resources\\tournamentView.png')
        self.matchTablePg = Label(self.master, image=self.img)
        self.matchTablePg.pack()
        self.teamname = {1:"MI",2:"CSK",3:"KKR",4:"DC",5:"RR",6:"RCB",7:"PKBS",8:"SRH"}

        self.style = ttk.Style()
        self.style.theme_use("vista")
        self.style.configure("matches.Treeview.Heading",
                             background="#efefef",
                             foreground="black",
                             rowheight=45,
                             fieldbackground="#d3d3d3",
                             font=('Yu Gothic', 20, 'bold')
                             )
        self.style.configure("matches.Treeview",
                             background="#d3d3d3",
                             foreground="black",
                             rowheight=38,
                             fieldbackground="#d3d3d3",
                             font=('Yu Gothic', 15, 'bold')
                             )
        # style.layout("matches.Treeview",[('table.Treeview.treearea', {'sticky': 'nswe'})]) #remove border
        self.style.map('Treeview', background=[('selected', '#caf6ff')])

        self.matches = ttk.Treeview(self.master, style="matches.Treeview")

        self.matches['columns'] = (
            "matchId", "date", "time", "venue", "homeTeam", "awayTeam", "result")
        self.matches['show'] = 'headings'
        self.matches.column("matchId", width=130, anchor='center')
        self.matches.column("date", width=130, anchor='center')
        self.matches.column("time", width=130, anchor='center')
        self.matches.column("venue", width=370, anchor='center')
        self.matches.column("homeTeam", width=250, anchor='center')
        self.matches.column("awayTeam", width=250, anchor='center')
        self.matches.column("result", width=160, anchor='center')

        self.matches.heading("matchId", text="Match Id")
        self.matches.heading("date", text="Date")
        self.matches.heading("time", text="Time")
        self.matches.heading("venue", text="Venue")
        self.matches.heading("homeTeam", text="Home Team")
        self.matches.heading("awayTeam", text="Away Team")
        self.matches.heading("result", text="Add Result")

        self.container = ttk.Frame(self.master)
        self.canvas = Canvas(self.container, width=1400,
                             height=700, background="grey")
        self.scrollbar = ttk.Scrollbar(
            self.container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all"),
                height=375,
            )
        )

        self.canvas.create_window(
            (0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(
            yscrollcommand=self.scrollbar.set, background="grey")

        self.matchList = matchesList

        self.msg = matchesList[0][0]
        self.t_id = Message(self.master, text=self.msg,
                            background="white", font=('Yu Gothic', 15, 'bold'))
        self.t_id.place(x=1363, y=182, width=80)

        for i in range(len(self.matchList)):
            self.row = Label(self.scrollable_frame, width=201,
                             height=3, background="#d9d9d9")
            self.row.pack(pady=3)
            self.edtBtn = Button(self.row, width=10, background='#caf6ff',
                                 relief='groove', text='Result', font=('Yu Gothic', 10, 'bold'), command= lambda id=[self.matchList[i][1],self.teamname[int(self.matchList[i][5])],self.teamname[int(self.matchList[i][6])]]: self.fillResult(id))
            self.edtBtn.place(x=1300, y=7)
            self.m_id = Label(self.row, width=7, height=1, background="#d9d9d9",
                              text=self.matchList[i][1], font=('Yu Gothic', 14, 'bold'))
            self.m_id.place(x=4, y=5)
            self.date_lbl = Label(self.row, width=9, height=1, background="#d9d9d9",
                                  text=self.matchList[i][2], font=('Yu Gothic', 14, 'bold'))
            self.date_lbl.place(x=134, y=5)
            self.time_lbl = Label(self.row, width=9, height=1, background="#d9d9d9",
                                  text=self.matchList[i][3].strftime("%H:%M:%S"), font=('Yu Gothic', 14, 'bold'))
            self.time_lbl.place(x=270, y=5)
            self.venue_lbl = Label(self.row, width=25, height=1, background="#d9d9d9", text=self.matchList[i][4],
                                   font=('Yu Gothic', 14, 'bold'))
            self.venue_lbl.place(x=420, y=5)
            self.homeTeam_lbl = Label(self.row, width=15, height=1, background="#d9d9d9",
                                      text=self.teamname[int(self.matchList[i][5])], font=('Yu Gothic', 14, 'bold'))
            self.homeTeam_lbl.place(x=790, y=5)
            self.awayTeam_lbl = Label(self.row, width=15, height=1, background="#d9d9d9",
                                      text=self.teamname[int(self.matchList[i][6])], font=('Yu Gothic', 14, 'bold'))
            self.awayTeam_lbl.place(x=1029, y=5)

        self.container.place(x=61, y=278)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.matchbackBtn = Button(self.master, width=15, background='#caf6ff',
                                   relief='flat', text='Back', font=('Yu Gothic', 18, 'bold'), command=self.back)
        self.matchbackBtn.place(x=120, y=720)

        self.ptsTableBtn = Button(self.master, width=15, background='#caf6ff',
                                  relief='flat', text='Points Table', font=('Yu Gothic', 18, 'bold'), command=self.ptsView)
        self.ptsTableBtn.place(x=1270, y=720)

        self.matches.place(x=60, y=240)
        self.master.mainloop()

# maintournamentView()
