from tkinter import *
from tkinter import ttk
from initial import initialize
initialize()
from connect import *



# def main7():
#   r = Tk(className=" CTDMS View Result")
#   app=ViewResult(r)

class ViewResult:

    def back(self):
      self.master.destroy()

    def __init__(self,master,team_id):
      self.master=master
      self.width=self.master.winfo_screenwidth()
      self.height=self.master.winfo_screenheight()
      self.master.geometry("%dx%d+0+0"%(self.width,self.height))
      self.master.state('zoomed')
<<<<<<< HEAD
=======
      
>>>>>>> 30d7f637b427821f921263ff54410ad8cc1b4b18
      self.img = PhotoImage(file='resources\\resultView.png')
      self.matchResultPg = Label(self.master, image=self.img)
      self.matchResultPg.pack()

      self.t_id = team_id

      self.style = ttk.Style()
      self.style.theme_use("vista")
      self.style.configure("result.Treeview.Heading",
                        background="#e7e7e5",
                        foreground="black",
                        rowheight=48,
                        fieldbackground="#e7e7e5",
                        font=('Yu Gothic', 20, 'bold')
                        )
      self.style.configure("result.Treeview",
                        background="#e7e7e5",
                        foreground="black",
                        rowheight=43,
                        fieldbackground="#d3d3d3",
                        font=('Yu Gothic', 15, 'bold'))
      # style.layout("result.Treeview",[('result.Treeview.treearea', {'sticky': 'nswe'})]) #remove border
      self.style.map('Treeview', background=[('selected', '#f4a209')])

      self.result = ttk.Treeview(self.master, style="result.Treeview")

      self.scrlbar = ttk.Scrollbar(self.result,orient="vertical", command=self.result.yview)
      self.scrlbar.place(x=1425, y=36, height=430)
      self.result.configure(xscrollcommand=self.scrlbar.set)

      self.result['columns'] = ("1", "2", "3", "4", "5", "6", "7", "8")
      self.result['show'] = 'headings'     # to_remove_empty_column
      self.result.column("1", width=120, anchor='center')
      self.result.column("2", width=170, anchor='center')
      self.result.column("3", width=200, anchor='center')
      self.result.column("4", width=200, anchor='center')
      self.result.column("5", width=150, anchor='center')
      self.result.column("6", width=200, anchor='center')
      self.result.column("7", width=200, anchor='center')
      self.result.column("8", width=200, anchor='center')

      self.result.heading("1", text="M Id")
      self.result.heading("2", text="Date")
      self.result.heading("3", text="Opponent")
      self.result.heading("4", text="TossWon")
      self.result.heading("5", text="Choose To")
      self.result.heading("6", text="1st Inning")
      self.result.heading("7", text="2nd Inning")
      self.result.heading("8", text="Winner")

      self.result.place(x=42,y=185) 

      self.matchResults = matchResult(self.t_id)
      for i in self.matchResults:
        self.result.insert(parent='', index='end', iid=i, values=(i[0] ,i[1], i[2], i[3], i[4], i[5], i[6], i[7]))

      self.backBtn = Button(self.master,width=10, background='#f4a290', relief='flat', text='Back',foreground="white", font=('Yu Gothic', 15, 'bold'),
                              command=self.back)
      self.backBtn.place(x=145, y=734)
      self.master.mainloop()

# main7()