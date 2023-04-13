import random
def lista():
      palabra=["Callejon","Esternocleidomastoideo","Saludar","Manzanera"]
      random.shuffle(palabra)   
      return (palabra[0])
       

def bondia():
      print (lista())
      if lista() == "Manzanera":
            print("Hola")
bondia()




