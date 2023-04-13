import random

print("Hola! Anem a jugar al trivial")

preguntes = [["¿En qué año el hombre pisó la Luna por primera vez? \n1. 1969 \n2. 1958\n3. 1869\n", 1],
             ["¿Cuánto duró la Guerra de los Cien Años? \n1. 154 \n2. 116\n3. 100\n", 2],
             ["¿Quién fue el primer presidente de la democracia española tras el franquismo? \n1. Mariano Rajoy \n2. Adolfo Suarez\n3. Pedro Sanchez\n", 2],
             ["¿Cuál es el río más caudaloso del mundo? \n1. Cervol \n2. Nilo\n3. Amazonas\n", 3],
             ["¿Cuál es el monte más alto del mundo? \n1. Everest \n2. K2\n3. Kilimanjaro\n", 1],
             ["¿Cuál es la capital de Perú? \n1. Buenos Aires \n2. Lima\n3. Ciudad del Vaticano\n", 2],
             ["¿A quién interpretaba John Travolta en “Grease”? \n1. Danny Zuko \n2. Michel Night\n3. Abraham Lincon\n", 1],
             ["¿Quién fue el famoso cantante del grupo musical Queen? \n1. Freddie Mercury \n2. RVFV\n3. Manolo Escobar\n", 1],
             ["¿Quién pintó el “Guernica”? \n1. Leonardo Da Vinci \n2. Rafael\n3. Pablo Picasso\n", 3],
             ["¿Qué nombre tenía el caballo de Don Quijote de la Mancha? \n1. Rocinante \n2. Perdigón\n3. Babieca\n", 1],
             ["¿Cuál es el piloto de MotoGP nacido en España que más campeonatos ha conseguido? \n1. Valentino Rossi \n2.Marc Marquez \n3.Jorge Lorenzo\n", 2],
             ["¿Qué conocido boxeador inició su trayectoria profesional con el nombre de Cassius Clay? \n1. Myke Tyson \n2. Muhammad Ali \n3. Rocky Balboa", 2]]


random.shuffle(preguntes)

jugadors = ["jugador 1","jugador 2"]

random.shuffle(jugadors)

punts = [0,0]

print(jugadors)
print("\nEs el turno del", jugadors[0])

contador_preg = 0


for pregunta in preguntes:
    contador_preg += 1
    if(contador_preg != 10):
        print(contador_preg)
        preguntes.remove(pregunta)

        respuesta= int(input(pregunta[0]))
        
        if (contador_preg != 10):

                

            if (respuesta == pregunta[1]):
                print("Bien hecho")
                punts[0] += 1 
                print ("Tienes",punts[0], "aciertos")
                if (punts[0] == 3):
                    print("Ha ganado el ",jugadors[0])
                    break
                
            else:
                print("Has fallat")
            
                
                print("\nEs el turno del", jugadors[1])

                for pregunta in preguntes:
                    contador_preg += 1
                    print(contador_preg)
                    preguntes.remove(pregunta)
                    respuesta= int(input(pregunta[0]))

                    if (respuesta == pregunta[1]):
                        print("Bien hecho")
                        punts[1] += 1 
                        print ("Tienes",punts[1], "aciertos")
                        if (punts[1] == 3):
                            print("Ha ganado el ",jugadors[1])
                            break
                            

                    if (respuesta != pregunta[1]):
                        print("\nEs el turno del", jugadors[0])
                        break
                    
    else:
        print("Has hecho 10 preguntas, se ha acabado el juego")