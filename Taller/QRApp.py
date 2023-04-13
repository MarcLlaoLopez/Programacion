#sudo apt-get install python3-tk
from tkinter import *
#pip3 install png
import pyqrcode 
#pip3 install pypng
import png


def pintaqr():
      global my_qr

      url=pyqrcode.create(ent1.get())
      url.png('elmeuqr.png', scale = 6)
      url=url.xbm(scale=5)
      my_qr=BitmapImage(data=url)
      l2.config(image=my_qr)


win = Tk()
win.geometry("640x400")
win.configure(bg = 'white')
win.title('Aplicació tKinter')

l1 = Label(win,text="Aplicació Print!", background="black", foreground="white", width=80, border= 10, anchor="center")
l1.grid(column=0,row=0)
l2 = Label(win,text='El QR es mostrarà aquí')
l2.grid(column=0,row=2)

ent1 = Entry(win)
ent1.grid(column=0,row=3)

btn2 = Button(text="Generar", command=pintaqr)
btn2.grid(column=0,row=4)
btn1 = Button(text="Sortir", command=win.destroy)
btn1.grid(column=0,row=8)


win.mainloop()