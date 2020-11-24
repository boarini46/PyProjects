from tkinter import Tk, Button, Label
from tkinter.messagebox import showinfo
from time import strftime, localtime

def clicked():
    time = strftime('Dia: %d %b %Y %A\nHorário Local: %H:%M:%S\n', localtime())
    #showinfo(message=time)
    lb["text"] = time

root = Tk()
root.geometry("250x100")
root.title("Hora Local - BR")
button = Button(root, text='TimeZone', command=clicked)
button.pack()

lb = Label(root, text='')
lb.place(x=50, y=50)

root.mainloop() 
