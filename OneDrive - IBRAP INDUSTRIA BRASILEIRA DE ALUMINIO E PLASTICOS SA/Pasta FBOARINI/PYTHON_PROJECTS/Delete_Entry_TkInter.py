from tkinter import *
from tkinter import ttk
from calendar import DateEntry

def clearDateEntry():
    clearButton.focus_set()
    myDateEntry.delete(0,END)

root=Tk()

myDateEntry=DateEntry(root)
myDateEntry.pack()
myDateEntry.delete(0,END)

clearButton=Button(root,text='clear',command=clearDateEntry)
clearButton.pack()

root.mainloop()