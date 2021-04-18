from tkinter import *
from tkinter import ttk

r = Tk(className=" CTDMS Points Table")
r.geometry("1530x790")
img = PhotoImage(file='resources\\PointsTable.png')
pointsTablePg = Label(r, image=img)
pointsTablePg.pack()

msg = "Id"
t_id = Message(r, text=msg, background="white", font=('Yu Gothic', 15, 'bold'))
t_id.place(x=860, y=165, width=50)

style = ttk.Style()
style.theme_use("vista")
style.configure("table.Treeview.Heading",
                background="#d9d9d9",
                foreground="black",
                rowheight=48,
                fieldbackground="#d9d9d9",
                font=('Yu Gothic', 20, 'bold')
                )
style.configure("table.Treeview",
                background="#d9d9d9",
                foreground="black",
                rowheight=43,
                fieldbackground="#d9d9d9",
                font=('Yu Gothic', 15, 'bold'))
# style.layout("table.Treeview",[('table.Treeview.treearea', {'sticky': 'nswe'})]) #remove border
style.map('Treeview', background=[('selected', '#caf6ff')])

table = ttk.Treeview(r, style="table.Treeview")

scrlbar = ttk.Scrollbar(table,orient="vertical", command=table.yview)
scrlbar.place(x=1255, y=36, height=430)
table.configure(xscrollcommand=scrlbar.set)

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
table.insert(parent='', index='end', iid=1, values=("1", "csk", "14", "12", "2", "100"))
table.insert(parent='', index='end', iid=2, values=("1", "csk", "14", "12", "2", "100"))
table.insert(parent='', index='end', iid=3, values=("1", "csk", "14", "12", "2", "100"))
table.insert(parent='', index='end', iid=4, values=("1", "cskhfd", "14", "12", "2", "100"))
table.insert(parent='', index='end', iid=5, values=("1", "csk", "14", "12", "2", "100"))
table.insert(parent='', index='end', iid=6, values=("1", "csk", "14", "12", "2", "100"))
table.insert(parent='', index='end', iid=7, values=("1", "cskrt", "14", "12", "2", "100"))
table.insert(parent='', index='end', iid=8, values=("1", "cs5y5k", "14", "12", "2", "100"))
table.insert(parent='', index='end', iid=9, values=("1", "cskf", "14", "12", "2", "100"))
table.insert(parent='', index='end', iid=10, values=("1", "csghk", "14", "12", "2", "100"))
table.insert(parent='', index='end', iid=11, values=("1", "cghdfk", "14", "12", "2", "100"))
table.insert(parent='', index='end', iid=12, values=("1", "cfg", "14", "12", "2", "100"))



table.place(x=130, y=220)

backBtn = Button(width=10, background='#caf6ff', relief='flat', text='Back', font=('Yu Gothic', 18, 'bold'))
backBtn.place(x=1310, y=727)

r.mainloop()