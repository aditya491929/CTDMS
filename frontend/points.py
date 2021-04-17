from tkinter import *
from tkinter import ttk

r = Tk(className=" CTDMS Points Table")
r.geometry("1530x790")
img = PhotoImage(file='resources\\PointsTable.png')
pointsTablePg = Label(r, image=img)
pointsTablePg.pack()

style = ttk.Style()
style.theme_use("vista")
style.configure("table.Treeview.Heading",
                background="#efefef",
                foreground="black",
                rowheight=48,
                fieldbackground="#d3d3d3",
                font=('Yu Gothic', 20, 'bold')
                )
style.configure("table.Treeview",
                background="#d3d3d3",
                foreground="black",
                rowheight=43,
                fieldbackground="#d3d3d3",
                font=('Yu Gothic', 15, 'bold'))
# style.layout("table.Treeview",[('table.Treeview.treearea', {'sticky': 'nswe'})]) #remove border
style.map('Treeview', background=[('selected', '#caf6ff')])

table = ttk.Treeview(r, style="table.Treeview")

table['columns'] = ("1", "2", "3", "4", "5", '6')
table['show'] = 'headings'     # to_remove_empty_column
table.column("1", width=170, anchor='center')
table.column("2", width=420, anchor='center')
table.column("3", width=170, anchor='center')
table.column("4", width=170, anchor='center')
table.column("5", width=170, anchor='center')
table.column("6", width=170, anchor='center')


table.heading("1", text="Rank")
table.heading("2", text="Team")
table.heading("3", text="M")
table.heading("4", text="W")
table.heading("5", text="L")
table.heading("6", text="Pts")

table.insert(parent='', index='end', iid=0, values=("1", "csk", "14", "12", "2", "100"))

table.place(x=130, y=220)

backBtn = Button(width=10, background='#caf6ff', relief='flat', text='Back', font=('Yu Gothic', 18, 'bold'))
backBtn.place(x=1310, y=723)

r.mainloop()