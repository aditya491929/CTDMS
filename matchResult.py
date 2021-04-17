from tkinter import *

r = Tk(className=" CTDMS Match Result")
r.geometry("1530x790")
img = PhotoImage(file='resources\\matchResult.png')
matchResultPg = Label(r, image=img)
matchResultPg.pack()

matchNoEntry = Entry(font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
matchNoEntry.place(x=330, y=207, width=200)

tossEntry = Entry(font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
tossEntry.place(x=1106, y=207, width=200)

runs1Entry = Entry(font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
runs1Entry.place(x=100, y=388, width=200)

overs1Entry = Entry(font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
overs1Entry.place(x=447, y=388, width=200)

wickets1Entry = Entry(font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
wickets1Entry.place(x=100, y=513, width=200)

extras1Entry = Entry(font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
extras1Entry.place(x=447, y=513, width=200)


runs2Entry = Entry(font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
runs2Entry.place(x=875, y=388, width=200)

overs2Entry = Entry(font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
overs2Entry.place(x=1225, y=388, width=200)

wickets2Entry = Entry(font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
wickets2Entry.place(x=875, y=513, width=200)

extras2Entry = Entry(font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
extras2Entry.place(x=1225, y=513, width=200)


momEntry = Entry(font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
momEntry.place(x=270, y=633, width=200)

winEntry = Entry(font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
winEntry.place(x=730, y=633, width=200)

loseEntry = Entry(font=('Yu Gothic', 20), background='#d9d9d9', relief='flat')
loseEntry.place(x=1210, y=633, width=200)

saveBtn = Button(width=10, background='#7ed957', relief='flat', text='Save', font=('Yu Gothic', 18, 'bold'))
saveBtn.place(x=545, y=708)

backBtn = Button(width=10, background='#96ddf8', relief='flat', text='Back', font=('Yu Gothic', 18, 'bold'))
backBtn.place(x=845, y=708)
r.mainloop()
