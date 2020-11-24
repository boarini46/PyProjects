from tkinter import Tk, Button, Label, Entry,END
from tkinter.messagebox import showinfo
from time import strftime, strptime
#from datetime import date

def compute():
    #global entry
    global data1
    data1 = entry.get()
    #lb = Label(root)
    try:
        #lb.pack(pady=10)
        #lb.pack_forget()
        weekday = strftime('%A', strptime(data1, '%d/%m/%Y'))
        showinfo(message='{} was a {}'.format(data1, weekday))
    except:
        
        showinfo(message='Digite a data Corretamente! Try again...')
        delcont()

def delcont():
    data1.delete(1,'end')



root = Tk()
root.title("Data x Dia da semana")
root.geometry("300x100")
label = Label(root, text='Digite uma data: ')
label.grid(row=1, column=0)
entry = Entry(root)
entry.grid(row=1, column=1)
button = Button(root, text='Valida Data', command = compute)
button.grid(row=2, column=0, columnspan=2)
root.mainloop()