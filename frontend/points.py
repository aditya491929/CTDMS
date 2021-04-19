from tkinter import *
from tkinter import ttk
from initial import initialize
initialize()
from connect import validateAdmin,validateTeam


def main4():
  r = Tk(className=" CTDMS Points Table")
  app4=PointsTable(r)

class PointsTable:
    def __init__(self,master):
        self.master=master
        self.master.geometry("1530x790")
        self.img = PhotoImage(file='resources\\PointsTable.png')
        self.pointsTablePg = Label(self.master, image=self.img)
        self.pointsTablePg.pack()

        self.msg = "Id"
        self.t_id = Message(self.master, text=self.msg, background="white", font=('Yu Gothic', 15, 'bold'))
        self.t_id.place(x=860, y=165, width=50)

        self.style = ttk.Style()
        self.style.theme_use("vista")
        self.style.configure("table.Treeview.Heading",
                        background="#e7e7e5",
                        foreground="black",
                        rowheight=48,
                        fieldbackground="#e7e7e5",
                        font=('Yu Gothic', 20, 'bold')
                        )
        self.style.configure("table.Treeview",
                        background="#e7e7e5",
                        foreground="black",
                        rowheight=43,
                        fieldbackground="#e7e7e5",
                        font=('Yu Gothic', 15, 'bold'))
        # style.layout("table.Treeview",[('table.Treeview.treearea', {'sticky': 'nswe'})]) #remove border
        self.style.map('Treeview', background=[('selected', '#caf6ff')])

        self.table = ttk.Treeview(self.master, style="table.Treeview")

        self.scrlbar = ttk.Scrollbar(self.table,orient="vertical", command=self.table.yview)
        self.scrlbar.place(x=1255, y=36, height=430)
        self.table.configure(xscrollcommand=self.scrlbar.set)

        self.table['columns'] = ("1", "2", "3", "4", "5", '6')
        self.table['show'] = 'headings'     # to_remove_empty_column
        self.table.column("1", width=170, anchor='center')
        self.table.column("2", width=420, anchor='center')
        self.table.column("3", width=170, anchor='center')
        self.table.column("4", width=170, anchor='center')
        self.table.column("5", width=170, anchor='center')
        self.table.column("6", width=170, anchor='center')


        self.table.heading("1", text="Rank")
        self.table.heading("2", text="Team")
        self.table.heading("3", text="M")
        self.table.heading("4", text="W")
        self.table.heading("5", text="L")
        self.table.heading("6", text="Pts")

        self.table.insert(parent='', index='end', iid=0, values=("1", "csk", "14", "12", "2", "100"))
        self.table.insert(parent='', index='end', iid=1, values=("1", "csk", "14", "12", "2", "100"))
        self.table.insert(parent='', index='end', iid=2, values=("1", "csk", "14", "12", "2", "100"))
        self.table.insert(parent='', index='end', iid=3, values=("1", "csk", "14", "12", "2", "100"))
        self.table.insert(parent='', index='end', iid=4, values=("1", "cskhfd", "14", "12", "2", "100"))
        self.table.insert(parent='', index='end', iid=5, values=("1", "csk", "14", "12", "2", "100"))
        self.table.insert(parent='', index='end', iid=6, values=("1", "csk", "14", "12", "2", "100"))
        self.table.insert(parent='', index='end', iid=7, values=("1", "cskrt", "14", "12", "2", "100"))
        self.table.insert(parent='', index='end', iid=8, values=("1", "cs5y5k", "14", "12", "2", "100"))
        self.table.insert(parent='', index='end', iid=9, values=("1", "cskf", "14", "12", "2", "100"))
        self.table.insert(parent='', index='end', iid=10, values=("1", "csghk", "14", "12", "2", "100"))
        self.table.insert(parent='', index='end', iid=11, values=("1", "cghdfk", "14", "12", "2", "100"))
        self.table.insert(parent='', index='end', iid=12, values=("1", "cfg", "14", "12", "2", "100"))



        self.table.place(x=130, y=220)

        self.backBtn = Button(width=10, background='#caf6ff', relief='flat', text='Back', font=('Yu Gothic', 18, 'bold'))
        self.backBtn.place(x=1310, y=727)

        self.master.mainloop()

main4()