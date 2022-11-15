"""
Tasca 1:
Escriu un programa que sol·liciti una puntuació entre 0 i 10. Si la puntuació és fora d'aquest rang, mostra un missatge d'error.
 Si la puntuació està entre 0 i 10, mostra la qualificació usant la taula següent:
Puntuació Qualificació
>= 9 Excel·lent
>= 8 Notable
>= 7 Bé
>= 5 Suficient
< 5 Insuficient
Bateria de proves:
Introduïu puntuació: 9.5 -> Excel·lent
Introduïu puntuació: perfecte -> Puntuació incorrecta
Introduïu puntuació: 11 Puntuació -> Incorrecta
Introduïu puntuació: 7.5 -> Bé
Introduïu puntuació: 0.5 -> Insuficient
"""
print("Tasca 1")

try:
    puntuacio = float(input("Proporciona una puntuació entre 0 i 10: "))

    if (puntuacio < 0 or puntuacio > 10):
        print("Tens que introduir una puntuacio entre 0 i 10") 

    else:
        if (puntuacio >= 0 and puntuacio < 5):
            print("Insuficient")
        
        elif (puntuacio >= 5 and puntuacio < 7):
            print("Suficient")
        
        elif (puntuacio >= 7 and puntuacio < 8):
            print("Bé")

        elif (puntuacio >= 8 and puntuacio < 9):
            print("Notable")

        else:
            print("Excel·lent")
except:
    print("Tens que posar un numero")


"""
Tasca 2:
Escriu un programa que demani l'any actual i un altre any qualsevol. El resultat ha de mostrar quants anys han passat des de l'any introduït o quants anys falten.
Ara milloreu el programa per a fer que quan la diferència sigui només d'un any, ens digui que només falta un any.
"""

print ("Tasca 2")
try:

  any_actual = int(input("Escriu el any actual: "))
  any_elegit = int(input("Escriu el any que vullgues: "))
  
  

  if (any_actual > any_elegit):
    resultat1 = int(any_actual - any_elegit)
    
    if (resultat1 == 1):
        print("Ha passat", resultat1, "any")
    else:
        print("Han passat", resultat1, "anys")
    
  
  else:
    resultat2 = int(any_elegit - any_actual)
    if (resultat2 == 1):
        print("Queda", resultat2, "any")

    else:
        print("Queden", resultat2, "anys")

except:
    print("Tens que posar un numero")

"""
Tasca 3:
Creeu un joc de daus on es generi una tirada per a cadascun dels jugadors, quan escriguin la paraula "tirar" en un input i posteriorment es mostri el resultat de la partida.
Podeu utilitzar la funció randint() de la llibreria random:
Exemple d'ús:
import random
numero = random.randint(1, 6)
"""

import random


try:

    n_jugadors = int(input("Quants jugadors aneu a ser? (maxim 4 jugadors) :"))

    if (n_jugadors == 1):

        numero = random.randint(1, 6)
        tirada = str(input("Tens que escriure la paraula ""tirar"" per a començar: "))

        if (tirada == "tirar"):
            print("Has tret un", numero)
        else:
            print("No ho has escrit be")
    
    elif (n_jugadors == 2):
        
        print("Jugador 1")
        numero = random.randint(1, 6)
        tirada = str(input("Tens que escriure la paraula ""tirar"" per a començar: "))

        if (tirada == "tirar"):
            print("Has tret un", numero)
        
            print("Jugador 2")
            numero = random.randint(1, 6)
            tirada = str(input("Tens que escriure la paraula ""tirar"" per a començar: "))
            if (tirada == "tirar"):
                print("Has tret un", numero)
            else:
                print("No ho has escrit be")

        else:
            print("No ho has escrit be")
    
    elif (n_jugadors == 3):
        
        print("Jugador 1")
        numero = random.randint(1, 6)
        tirada = str(input("Tens que escriure la paraula ""tirar"" per a començar: "))

        if (tirada == "tirar"):
            print("Has tret un", numero)
        
            print("Jugador 2")
            numero = random.randint(1, 6)
            tirada = str(input("Tens que escriure la paraula ""tirar"" per a començar: "))
            if (tirada == "tirar"):
                print("Has tret un", numero)

                print("Jugador 3")
                numero = random.randint(1, 6)
                tirada = str(input("Tens que escriure la paraula ""tirar"" per a començar: "))
                if (tirada == "tirar"):
                    print("Has tret un", numero)
                
                else:
                  print("No ho has escrit be")
            else:
                print("No ho has escrit be")

        else:
            print("No ho has escrit be")

    elif (n_jugadors == 4):
        
        print("Jugador 1")
        numero = random.randint(1, 6)
        tirada = str(input("Tens que escriure la paraula ""tirar"" per a començar: "))

        if (tirada == "tirar"):
            print("Has tret un", numero)
        
            print("Jugador 2")
            numero = random.randint(1, 6)
            tirada = str(input("Tens que escriure la paraula ""tirar"" per a començar: "))
            if (tirada == "tirar"):
                print("Has tret un", numero)

                print("Jugador 3")
                numero = random.randint(1, 6)
                tirada = str(input("Tens que escriure la paraula ""tirar"" per a començar: "))
                if (tirada == "tirar"):
                    print("Has tret un", numero)

                    print("Jugador 4")
                    numero = random.randint(1, 6)
                    tirada = str(input("Tens que escriure la paraula ""tirar"" per a començar: "))
                    if (tirada == "tirar"):
                        print("Has tret un", numero)
                    
                    else:
                        print("No ho has escrit be")
                
                else:
                  print("No ho has escrit be")
            else:
                print("No ho has escrit be")

        else:
            print("No ho has escrit be")

except:
    print("Has de posar un numero del 1-4")
