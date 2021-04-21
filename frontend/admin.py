from createTournament import CreateTournament
from tournamentView import TourView
from tkinter import *
from tkinter import ttk
from initial import initialize
initialize()
from connect import *

# def main1():
#   r = Tk(className=" CTDMS Admin View")
#   app=adminWindow(r)


class AdminWindow:
    def createTour(self):
        self.r3 = Toplevel(self.master)
        self.app = CreateTournament(self.r3, self.adminId)

    def viewTour(self):
        tour_Id = self.tourId.get()
        self.tourId.set("")
        matchesList = getMatchesForAdmin(tour_Id)
        self.r2 = Toplevel(self.master)
        self.app = TourView(self.r2, matchesList)

    def logout(self):
        self.master.destroy()

    def __init__(self, master, adminId):
        self.master = master
        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        self.master.geometry("%dx%d+0+0" % (self.width, self.height))
        self.master.state('zoomed')

        self.img1 = PhotoImage(file='resources\\admin.png')
        self.adminViewPg = Label(self.master, image=self.img1)
        self.adminViewPg.pack()
        self.tourId = StringVar()
        self.adminId = adminId

        self.style = ttk.Style()
        self.style.theme_use("vista")
        self.style.configure("tournament.Treeview.Heading",
                             background="#efefef",
                             foreground="black",
                             rowheight=48,
                             fieldbackground="#d3d3d3",
                             font=('Yu Gothic', 12, 'bold')
                             )
        self.style.configure("tournament.Treeview",
                             background="#d3d3d3",
                             foreground="black",
                             rowheight=43,
                             fieldbackground="#d3d3d3",
                             font=('Yu Gothic', 10, 'bold'))
        # style.layout("table.Treeview",[('tournament.Treeview.treearea', {'sticky': 'nswe'})]) #remove border
        self.style.map('Treeview', background=[('selected', '#caf6ff')])

        self.tournaments = ttk.Treeview(
            self.master, style="tournament.Treeview")

        self.scrlbar = ttk.Scrollbar(
            self.tournaments, orient="vertical", command=self.tournaments.yview)
        self.scrlbar.place(x=1045, y=26, height=430)
        self.tournaments.configure(xscrollcommand=self.scrlbar.set)

        self.tournaments['columns'] = (
            "TournamentId", "TournamentName", "Host", "Year", "NumberOfMatches", "PrizeMoney", "Winner")
        self.tournaments['show'] = 'headings'
        self.tournaments.column("TournamentId", width=90, anchor="center")
        self.tournaments.column("TournamentName", width=250, anchor="center")
        self.tournaments.column("Host", width=170, anchor="center")
        self.tournaments.column("Year", width=100, anchor="center")
        self.tournaments.column("NumberOfMatches", width=150, anchor="center")
        self.tournaments.column("PrizeMoney", width=120, anchor="center")
        self.tournaments.column("Winner", width=180, anchor="center")

        self.tournaments.heading("TournamentId", text="Id")
        self.tournaments.heading("TournamentName", text="Tournament_name")
        self.tournaments.heading("Host", text="Host")
        self.tournaments.heading("Year", text="Year")
        self.tournaments.heading("NumberOfMatches", text="No_of_matches")
        self.tournaments.heading("PrizeMoney", text="Prize_money")
        self.tournaments.heading("Winner", text="Winner")

        self.tournaments.tag_configure('evenrow',background='#efefef')
        self.tournaments.tag_configure('oddrow',background='#d9d9d9')


        self.loadTournament = getTournaments()
        for i in range(len(self.loadTournament)):
            if i%2 == 0:
                self.tournaments.insert(parent='', index='end', iid=i, values=(self.loadTournament[i][0], self.loadTournament[i][1],
                                                                           self.loadTournament[i][2], self.loadTournament[i][3], 
                                                                           self.loadTournament[i][4], self.loadTournament[i][5],
                                                                           self.loadTournament[i][6]),tags=('evenrow',))
            else:
                self.tournaments.insert(parent='', index='end', iid=i, values=(self.loadTournament[i][0], self.loadTournament[i][1],
                                                                           self.loadTournament[i][2], self.loadTournament[i][3], 
                                                                           self.loadTournament[i][4], self.loadTournament[i][5],
                                                                           self.loadTournament[i][6]),tags=('oddrow',))
        self.tournaments.place(x=55, y=250)

        self.newTournamentBtn = Button(self.master, width=17, background='#caf6ff', relief='flat', text='Create New Tournament',
                                       font=('Yu Gothic', 14, 'bold'), wraplength=150, command=self.createTour)
        self.newTournamentBtn.place(x=1250, y=295)

        self.label1 = LabelFrame(
            self.master, text="Enter Tournament Id", background="#caf6ff")
        self.label1.place(x=1228, y=430, width=220, height=60)
        self.idEntry = Entry(self.label1, font=(
            'Yu Gothic', 14, 'bold'), textvariable=self.tourId)
        self.idEntry.place(x=10, y=0, width=200, height=40)
        self.viewTournamentBtn = Button(self.master, width=18, background='#caf6ff', relief='groove', text='View Tournament Matches',
                                        font=('Yu Gothic', 14, 'bold'), wraplength=200, command=self.viewTour)
        self.viewTournamentBtn.place(x=1225, y=505)

        self.adminLogoutBtn = Button(self.master, width=18, background='#ff5757', relief='flat', text='Logout',
                                     font=('Yu Gothic', 14, 'bold'), command=self.logout)
        self.adminLogoutBtn.place(x=1225, y=655)

        self.master.mainloop()

# main1()
