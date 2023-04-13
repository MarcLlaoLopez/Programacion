"""
def calcula_descompte(preu, descompte):
    return preu * (descompte/100)
print(calcula_descompte(int(input("Pon el precio: ")),int(input("Pon el descuento: "))))
"""

"""
x = "HOLA"
def abast():
    x="ADEU"
    print(x)
abast
print(x)
"""

"""
def presenta (nom,cognom,edat):
    print("Hola el meu nom és",nom, cognom, "i tinc",edat  )
"""

"""
presenta(nom="James", cognom="Bond", edat=48)
presenta(cognom="Morales", nom="Miles", edat=15)
"""

"""
def puntua(alumne,nota=0):
    print("Nom alumne:",alumne,"nota:",nota)
puntua("Enric")
puntua("Gullem",5)
puntua()
"""

"""8. Crida una funció que donat un string conti el número de ‘A’ o ‘a’ que conté aquest, fent un recorregut per la cadena de caràcters. Fes un programa que demani una entrada de text, que cridi a aquesta funció i en retorni el resultat al usuari en forma de “El número de A’s era: ”.

"""
"""
def numero(nom):
    contador = 0
    for i in nom:
            if i=="a" or i=="A":
                contador+=1    
            else:
                pass
    print(contador)


numero(str(input("Di un nombre")))
"""
"""10.Crea una funció que donat un string, comprovi si aquest es palindrom, això vol dir que es llegeixi d’igual manera d’esquerra a dreta que de dreta a esquerra (exemple: “Anna”, “Català, a l'atac”, “És així, ase”). Fes un programa que demani una entrada de text, que cridi a aquesta funció i n’informi al usuari"""
"""
def capicua(nom):
    lista=[nom]
    alreves= lista.reverse[0]
    print(lista, alreves)    
capicua(str(input("Di un nombre: ")))
"""

"""
def palindrom(cadena):
    cadena=list(cadena.replace(" ","").replace(",","").replace(".","").lower())
    rever=cadena.copy()
    rever.reverse()
    if cadena==rever:
        return True
    else:
        return False

def neteja(cadena):
    cadena=list(cadena.lower())
    prohibits=[".",","," "]
    x=0
    while(x<len(cadena)):
        if cadena[x] in prohibits:
            cadena.remove(cadena[x])
        else:
            x+=1
    return cadena
"""





"""
llista=["a","b","c"]

rever=llista.copy()
rever.reverse()
print(rever)
print(llista)
"""

from funcions import *

    










