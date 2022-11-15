import random

print("Hola! Anem a jugar al trivial")

preguntes = [["¿En qué año el hombre pisó la Luna por primera vez? \n1. 1969 \n2. 1958\n3. 1869\n", 1],
             ["¿Cuánto duró la Guerra de los Cien Años? \n1. 116 \n2. 158\n3. 100\n", 1],
             ["¿Quién fue el primer presidente de la democracia española tras el franquismo? \n1. Adolfo Suarez \n2. Mariano Rajoy\n3. Pedro Sanchez\n", 1],
             ["¿Cuál es el río más caudaloso del mundo? \n1. Amazonas \n2. Nilo\n3. Cervol\n", 1],
             ["¿Cuál es el monte más alto del mundo? \n1. Everest \n2. K2\n3. Kilimanjaro\n", 1],
             ["¿Cuál es la capital de Perú? \n1. Lima \n2. Buenos Aires\n3. Ciudad del Vaticano\n", 1],
             ["¿A quién interpretaba John Travolta en “Grease”? \n1. Danny Zuko \n2. Michel Night\n3. Abraham Lincon\n", 1],
             ["¿Quién fue el famoso cantante del grupo musical Queen? \n1. Freddie Mercury \n2. RVFV\n3. Manolo Escobar\n", 1],
             ["¿Quién pintó el “Guernica”? \n1. Pablo Picasso \n2. Rafael\n3. Leonardo Da Vinci\n", 1],
             ["¿Qué nombre tenía el caballo de Don Quijote de la Mancha? \n1. Rocinante \n2. Perdigón\n3. Babieca\n", 1]]


random.shuffle(preguntes)

jugadors = ["jugador 1","jugador 2"]

random.shuffle(jugadors)

ganar = int(3)
aciertos_j1 = 0
aciertos_j2 = 0


if (jugadors[0]):

    print("\nEs el turno del", jugadors[0])

    for pregunta in preguntes:
    
        respuesta= int(input(pregunta[0]))

        if (respuesta == pregunta[1]):
            print("Bien hecho")
            aciertos_j1=aciertos_j1 + 1
            print ("Tienes",aciertos_j1, "aciertos")
            if (aciertos_j1 == ganar):
                print("Has ganado")
                break

            else:
                print("Has fallat")

        elif (jugadors[1]):
            
            print("\nEs el turno del jugador 2\n")

            for pregunta in preguntes:
    
                respuesta= int(input(pregunta[0]))

