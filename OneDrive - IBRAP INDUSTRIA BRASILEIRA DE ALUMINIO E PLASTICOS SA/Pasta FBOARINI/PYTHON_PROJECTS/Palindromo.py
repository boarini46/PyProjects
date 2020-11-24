

from tkinter import *

def bt_onclick():
    #print(ed.get())

    g = ed.get()
    g.lower()
    
    i = g.replace(' ','')
    f = i[::-1]
    
    if i == f: # g[::-1] inverte a frase / palavras de trás pra frente
        lb["text"] =  'A frase é palíndromo --> %s'%(g[::-1])
    else:
        #print('A frase não é palíndromo --> %s'%(f))
        lb["text"] = 'A frase não é palíndromo --> %s'%(g[::-1])


    #lb["text"] = ed.get()


janela = Tk()
janela.title('Palíndromo')
janela.geometry("500x300")

ed = Entry(janela, width=60)
edlb = Label(janela,text = 'Palavra ou Frase:')
edlb.place(x=1,y=100)
ed.place(x=100, y=100)

#f = input('Digite uma frase:  ')

bt = Button(janela,width = 18,text = 'Verificar',command=bt_onclick)
bt.place(x=100, y=150)

lb = Label(janela)#, text='teste')
lb.place(x=100, y=200)

janela.mainloop()

'''
g = form.lower
g = f.lower().strip().replace(' ','')

if g == g[::-1]: # g[::-1] inverte a frase / palavras de trás pra frente
    resultado = Label(janela, text = 'A frase é palíndromo --> %s'%(f))
else:
    #print('A frase não é palíndromo --> %s'%(f))
    resultado = Label(janela, text = 'A frase não é palíndromo --> %s'%(f))


'''


