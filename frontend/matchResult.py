from tkinter import *
from tkinter import ttk
from initial import initialize
initialize()
from connect import *


# def main6():
#   r = Tk(className=" CTDMS Match Result")
#   app=MatchResult(r)

class MatchResult:
    def back(self):
      self.master.destroy()

    def giveResult(self):
      m_id = self.matchNo.get()
      tossWon = self.toss.get()
      run1 = self.runs1.get()
      over1 = self.overs1.get()
      wicket1 = self.wickets1.get()
      extra1 = self.extras1.get()
      run2 = self.runs2.get()
      over2 = self.overs2.get()
      wicket2 = self.wickets2.get()
      extra2 = self.extras2.get()
      manOfMatch = self.mom.get()
      winner = self.win.get()
      loser = self.lose.get()

      result = addMatchResult(m_id,tossWon,run1,over1,wicket1,extra1,run2,over2,wicket2,extra2,manOfMatch,winner,loser)
      if result:
        messagebox.showinfo(" Message","Match Result Added Successfully!")
      else:
        messagebox.showerror("Incomplete Details","All Fields Are Required!")


    def __init__(self,master,m_id):
      self.master=master
      self.master.geometry("1530x790")
      self.img = PhotoImage(file='resources\\matchResult.png')
      self.matchResultPg = Label(self.master, image=self.img)
      self.matchResultPg.pack()

      self.matchId = m_id

      self.toss = StringVar()
      self.runs1 = StringVar()
      self.overs1 = StringVar()
      self.wickets1 = StringVar()
      self.extras1 = StringVar()
      self.runs2 = StringVar()
      self.overs2 = StringVar()
      self.wickets2 = StringVar()
      self.extras2 = StringVar()
      self.mom = StringVar()
      self.win = StringVar()
      self.lose = StringVar()

      self.matchNoEntry = Message(self.master,font=('Yu Gothic', 20), text=self.matchId, background='#d9d9d9', relief='flat')
      self.matchNoEntry.place(x=330, y=203, width=200)

      self.tossEntry = Entry(self.master,font=('Yu Gothic', 20), textvariable=self.toss, background='#d9d9d9', relief='flat')
      self.tossEntry.place(x=1106, y=207, width=200)

      self.runs1Entry = Entry(self.master,font=('Yu Gothic', 20), textvariable=self.runs1, background='#d9d9d9', relief='flat')
      self.runs1Entry.place(x=100, y=388, width=200)

      self.overs1Entry = Entry(self.master,font=('Yu Gothic', 20), textvariable=self.overs1, background='#d9d9d9', relief='flat')
      self.overs1Entry.place(x=447, y=388, width=200)

      self.wickets1Entry = Entry(self.master,font=('Yu Gothic', 20), textvariable=self.wickets1, background='#d9d9d9', relief='flat')
      self.wickets1Entry.place(x=100, y=513, width=200)

      self.extras1Entry = Entry(self.master,font=('Yu Gothic', 20), textvariable=self.extras1, background='#d9d9d9', relief='flat')
      self.extras1Entry.place(x=447, y=513, width=200)


      self.runs2Entry = Entry(self.master,font=('Yu Gothic', 20), textvariable=self.runs2, background='#d9d9d9', relief='flat')
      self.runs2Entry.place(x=875, y=388, width=200)

      self.overs2Entry = Entry(self.master,font=('Yu Gothic', 20), textvariable=self.overs2, background='#d9d9d9', relief='flat')
      self.overs2Entry.place(x=1225, y=388, width=200)

      self.wickets2Entry = Entry(self.master,font=('Yu Gothic', 20), textvariable=self.wickets2, background='#d9d9d9', relief='flat')
      self.wickets2Entry.place(x=875, y=513, width=200)

      self.extras2Entry = Entry(self.master,font=('Yu Gothic', 20), textvariable=self.extras2, background='#d9d9d9', relief='flat')
      self.extras2Entry.place(x=1225, y=513, width=200)

      self.momSelect = ttk.Combobox(self.master,width=20, font=('Yu Gothic', 20), background="#d9d9d9")
      self.momSelect['values'] = ('Batsman',
                                'Bowler',
                                'All Rounder'
                                )
      self.momSelect.place(x=270, y=633,width=200)
      self.momSelect.current()

      # self.momEntry = Entry(self.master,font=('Yu Gothic', 20), textvariable=self.mom, background='#d9d9d9', relief='flat')
      # self.momEntry.place(x=270, y=633, width=200)

      self.winSelect = ttk.Combobox(self.master,width=20, font=('Yu Gothic', 20), background="#d9d9d9")
      self.winSelect['values'] = ('Batsman',
                                'Bowler',
                                'All Rounder'
                                )
      self.winSelect.place(x=730, y=633,width=200)
      self.winSelect.current()

      # self.winEntry = Entry(self.master,font=('Yu Gothic', 20), textvariable=self.win, background='#d9d9d9', relief='flat')
      # self.winEntry.place(x=730, y=633, width=200)

      self.loseSelect = ttk.Combobox(self.master,width=20, font=('Yu Gothic', 20), background="#d9d9d9")
      self.loseSelect['values'] = ('Batsman',
                                'Bowler',
                                'All Rounder'
                                )
      self.loseSelect.place(x=1210, y=633,width=200)
      self.loseSelect.current()

      # self.loseEntry = Entry(self.master,font=('Yu Gothic', 20), textvariable=self.lose, background='#d9d9d9', relief='flat')
      # self.loseEntry.place(x=1210, y=633, width=200)

      self.saveBtn = Button(self.master,width=10, background='#7ed957', relief='flat', text='Save', font=('Yu Gothic', 18, 'bold'))
      self.saveBtn.place(x=545, y=708)

      self.backBtn = Button(self.master,width=10, background='#96ddf8', relief='flat', text='Back', font=('Yu Gothic', 18, 'bold'),
                              command=self.back)
      self.backBtn.place(x=845, y=708)
      self.master.mainloop()

# main6()