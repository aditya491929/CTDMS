from tkinter import *
from tkinter import ttk
from initial import initialize
initialize()
from connect import validateAdmin,validateTeam


def main5():
  r = Tk(className=" CCTDMS Team View")
  app=TeamView(r)

class TeamView:
    def __init__(self,master):
        self.master=master
        self.master.geometry("1530x790")
        self.img = PhotoImage(file='resources\\teamView.png')
        self.teamViewPg = Label(self.master, image=self.img)
        self.teamViewPg.pack()

        self.msg = "11"
        self.t_id = Message(self.master, text=self.msg, background="#ffbcad", font=('Yu Gothic', 20, 'bold'),foreground="white")
        self.t_id.place(x=980, y=610, width=22)

        self.style = ttk.Style()
        self.style.theme_use("vista")
        self.style.configure("upcomingMatches.Treeview.Heading",
                        background="#efefef",
                        foreground="black",
                        rowheight=45,
                        fieldbackground="#d3d3d3",
                        font=('Yu Gothic', 20, 'bold')
                        )
        self.style.configure("upcomingMatches.Treeview",
                        background="#d3d3d3",
                        foreground="black",
                        rowheight=35,
                        fieldbackground="#d3d3d3",
                        font=('Yu Gothic', 15, 'bold')
                        )
        # style.layout("upcomingMatches.Treeview",[('table.Treeview.treearea', {'sticky': 'nswe'})]) #remove border
        self.style.map('Treeview', background=[('selected', '#caf6ff')])

        self.upcomingMatches = ttk.Treeview(self.master, style="upcomingMatches.Treeview")



        self.upcomingMatches['columns'] = ("opponent", "date", "time", "venue")
        self.upcomingMatches['show'] = 'headings'
        self.upcomingMatches.column("opponent", width=180, anchor='center')
        self.upcomingMatches.column("date", width=140, anchor='center')
        self.upcomingMatches.column("time", width=130, anchor='center')
        self.upcomingMatches.column("venue", width=250, anchor='center')

        self.upcomingMatches.heading("opponent", text="Opponent")
        self.upcomingMatches.heading("date", text="Date")
        self.upcomingMatches.heading("time", text="Time")
        self.upcomingMatches.heading("venue", text="Venue")

        self.container = ttk.Frame(self.master)
        self.canvas = Canvas(self.container, width=700, bg="white")
        self.scrollbar = ttk.Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all"),
                height=333
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=self.scrollbar.set, background="grey")


        for i in range(10):
            row = Label(self.scrollable_frame,width=99, height=3, background="#d9d9d9")
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
            

        self.container.place(x=46, y=300)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.upcomingMatches.place(x=45, y=250)

        self.style = ttk.Style()
        self.style.theme_use("vista")
        self.style.configure("player.Treeview.Heading",
                        background="#efefef",
                        foreground="black",
                        rowheight=40,
                        fieldbackground="#d3d3d3",
                        font=('Yu Gothic', 20, 'bold')
                        )
        self.style.configure("player.Treeview",
                        background="#d3d3d3",
                        foreground="black",
                        rowheight=31,
                        fieldbackground="#d3d3d3",
                        font=('Yu Gothic', 15, 'bold')
                        )
        # style.layout("player.Treeview",[('table.Treeview.treearea', {'sticky': 'nswe'})]) #remove border
        self.style.map('Treeview', background=[('selected', '#caf6ff')])

        self.player = ttk.Treeview(self.master, style="player.Treeview")

        self.player['columns'] = ("name", "type", "selected")
        self.player['show'] = 'headings'
        self.player.column("name", width=280, anchor='center')
        self.player.column("type", width=230, anchor='center')
        self.player.column("selected", width=130, anchor='center')

        self.player.heading("name", text="Name")
        self.player.heading("type", text="Player Type")
        self.player.heading("selected", text="Selected")

        self.container1 = ttk.Frame(self.master)
        self.canvas1 = Canvas(self.container1, width=637, bg="white")
        self.scrollbar1 = ttk.Scrollbar(self.container1, orient="vertical", command=self.canvas1.yview)
        self.scrollable_frame1 = ttk.Frame(self.canvas1)

        self.scrollable_frame1.bind(
            "<Configure>",
            lambda e1: self.canvas1.configure(
                scrollregion=self.canvas1.bbox("all"),
                height=293
            )
        )

        self.canvas1.create_window((0, 0), window=self.scrollable_frame1, anchor="nw")

        self.canvas1.configure(yscrollcommand=self.scrollbar1.set, background="grey")

        for i in range(10):
            row1 = Label(self.scrollable_frame1,width=90, height=3, background="#d9d9d9")
            row1.pack(pady=3)
            name = Label(row1, width=20, height=1, background="#d9d9d9", text="suryakumar yadav", font=('Yu Gothic', 14, 'bold'))
            name.place(x=10, y=6)
            type = Label(row1, width=12, height=1, background="#d9d9d9", text="Batsman", font=('Yu Gothic', 14, 'bold'))
            type.place(x=320, y=6)
            selected = Checkbutton(row1, background="#d9d9d9")
            selected.place(x=550, y=8)

        self.container1.place(x=824, y=300)
        self.canvas1.pack(side="left", fill="both", expand=True)
        self.scrollbar1.pack(side="right", fill="y")



        self.player.place(x=820, y=250)

        self.squadSaveBtn = Button(self.master,width=12, background='#ffbcad', relief='flat', text='Save', font=('Yu Gothic', 16, 'bold'),
                            foreground="white")
        self.squadSaveBtn.place(x=1267, y=612)

        self.teamLogoutBtn = Button(self.master,width=15, background='#f4a290', relief='flat', text='Logout', font=('Yu Gothic', 18, 'bold'),
                            foreground="white")
        self.teamLogoutBtn.place(x=100, y=722)

        self.addPlayerBtn = Button(self.master,width=17, height=1, background='#f4a290', relief='flat', text='Add Player', font=('Yu Gothic', 18, 'bold'),
                            foreground="white")
        self.addPlayerBtn.place(x=660, y=722)

        self.ptsTableBtn = Button(self.master,width=15, background='#f4a290', relief='flat', text='Points Table', font=('Yu Gothic', 18, 'bold'),
                            foreground="white")
        self.ptsTableBtn.place(x=1260, y=722)
        self.master.mainloop()

main5()