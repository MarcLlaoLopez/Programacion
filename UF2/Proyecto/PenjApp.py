from tkinter import *
# sudo apt-get install python3-pil python3-pil.imagetk
from PIL import Image, ImageTk
import random

num=1


 


win = Tk()
win.geometry("620x400")
win.configure(bg = 'white')
win.title('Aplicació PenjAPP Marc, Alex, Yassin')

l1 = Label(text="Aplicació PenjAPP Marc, Alex, Yassin", background="black", foreground="white", width=80, border= 10, anchor="center")
l1.grid(column=0,row=0,columnspan=2)

l2 = Label(text='La imatge es mostrarà aquí')
l2.grid(column=0,row=1,columnspan=2)


puntuacion1 = 0
puntuacion2 = 0
marcador = puntuacion1, "-" ,puntuacion2

#Obtenir una paraula random de la llista (llista amb paraules a resoldre pel jugador)
def lista():
      palabra=["callejon","esternocleidomastoideo","saludar","manzanera"]
      random.shuffle(palabra)   
      return (palabra[0])
      



btn2 = Button(text="Vamos a jugar", command=lambda:ahorcado())
btn2.grid(column=0,row=3,sticky=E)

letras_introducidas = []



palabra = list(lista())
print (palabra)


def ahorcado():

      
      
      def comprobar_letra():
            global num
            global palabra
            entrada = ent1.get()
            if len(entrada) == 1 and entrada.isalpha() and entrada not in letras_introducidas:
                  letras_introducidas.append(entrada)
                  if entrada in palabra:
                        print("Letra introducida correctamente.")
                        for i, letra in enumerate(palabra):
                         if letra == entrada:
                              palabra_guion[i] = str(letra)
                              l3.config(text=" ".join(palabra_guion))
                  else:
                        num += 1
            elif entrada in letras_introducidas:
                  print("La letra ya ha sido introducida anteriormente")
            else:
                  print("Introduzca una unica letra alfabetica")
           

      
                  
      #Pintar la forca, amb l'estat del jugador
      def pinta():
            global img
            global num
            if num > 9:
                  perder=("Has perdido. La palabra correcta era:", "".join(palabra))
                  l3 = Label(text=perder)
                  l3.grid(column=0,row=7,columnspan=2)

                  btn2 = Button(text="Jugar de nuevo", command=reiniciar_juego)
                  btn2.grid(column=0,row=3,sticky=E)
                  
            else:
                  img = Image.open("foto" + str(num) + ".jpg")
                  img = img.resize((300, 150))
                  img = ImageTk.PhotoImage(img)
                  l2.config(image=img)
            
            
      def pinta_com():
            comprobar_letra()
            if "_" not in palabra_guion:
                  ganar=("¡Felicidades, has ganado!")
                  l3 = Label(text=ganar)
                  l3.grid(column=0,row=7,columnspan=2)

                  btn2 = Button(text="Jugar de nuevo", command=reiniciar_juego)
                  btn2.grid(column=0,row=3,sticky=E)
                  
            else:
                  pinta()
            

      def reiniciar_juego():
            global num
            global letras_introducidas
            global palabra
            letras_introducidas = []
            palabra = list(lista())
            global palabra_guion
            palabra_guion = ["_" for letra in palabra]
            l3.config(text=" ".join(palabra_guion))
            btn2 = Button(text="Prueba suerte", command=pinta_com)
            btn2.grid(column=0,row=3,sticky=E)
            num = 1
            pinta()

      
      global palabra
      
      l3 = Label(text=palabra_guion)
      l3.grid(column=0,row=4,columnspan=2)

      l4 = Label(text=marcador)
      l4.grid(column=0,row=5,columnspan=4)

      ent1 = Entry()
      ent1.grid(column=0,row=2,columnspan=2)


      btn2 = Button(text="Prueba suerte", command=pinta_com)
      btn2.grid(column=0,row=3,sticky=E)
      btn1 = Button(text="Sortir", command=win.destroy)
      btn1.grid(column=1,row=3,sticky=W)
      
      pinta()

palabra_guion = ["_" for letra in palabra]


win.mainloop()
