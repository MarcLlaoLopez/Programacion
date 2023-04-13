#sudo apt-get install python3-tk

from tkinter import *

def pintar():
      vtext.set(ent1.get())  


win = Tk()
win.geometry("640x400")
win.configure(bg = 'white')
win.title('Aplicació tKinter')

l1 = Label(text="Aplicació Print!", background="black", foreground="white", width=80, border= 10, anchor="center")
l1.grid(column=0,row=0)

vtext = StringVar()
vtext.set("String de prova per variable")

l2 = Label(textvariable=vtext)
l2.grid(column=0,row=2)

ent1 = Entry(win)
ent1.grid(column=0,row=3)


btn2 = Button(text="Pintar", command=pintar)
btn2.grid(column=0,row=4)
btn1 = Button(text="Sortir", command=win.destroy)
btn1.grid(column=0,row=8)

win.mainloop()