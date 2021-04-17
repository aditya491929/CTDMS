from tkinter import *
from tkinter import ttk

r = Tk(className=" CTDMS Admin View")
r.geometry("1530x790")
img = PhotoImage(file='resources\\admin.png')
adminViewPg = Label(r, image=img)
adminViewPg.pack()