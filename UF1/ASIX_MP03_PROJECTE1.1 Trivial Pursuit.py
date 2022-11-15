import random

print("Hola! Anem a jugar al trivial")

preguntes = [["¿En qué año el hombre pisó la Luna por primera vez?", "\n1. 1969, \n2. 1958,\n3. 1869", 1],
             ["¿Cuánto duró la Guerra de los Cien Años?", "\n1. 116, \n2. 158,\n3. 100", 1],
             ["¿Quién fue el primer presidente de la democracia española tras el franquismo?", "\n1. Adolfo Suarez, \n2. Mariano Rajoy,\n3. Pedro Sanchez", 1],
             ["¿Cuál es el río más caudaloso del mundo?", "\n1. Amazonas, \n2. Nilo,\n3. Cervol", 1],
             ["¿Cuál es el monte más alto del mundo?", "\n1. Everest, \n2. K2,\n3. Kilimanjaro", 1],
             ["¿Cuál es la capital de Perú?", "\n1. Lima, \n2. Buenos Aires,\n3. Ciudad del Vaticano", 1],
             ["¿A quién interpretaba John Travolta en “Grease”?", "\n1. Danny Zuko, \n2. Michel Night,\n3. Abraham Lincon", 1],
             ["¿Quién fue el famoso cantante del grupo musical Queen?", "\n1. Freddie Mercury, \n2. RVFV,\n3. Manolo Escobar", 1],
             ["¿Quién pintó el “Guernica”?", "\n1. Pablo Picasso, \n2. Rafael,\n3. Leonardo Da Vinci", 1],
             ["¿Qué nombre tenía el caballo de Don Quijote de la Mancha?", "\n1. Rocinante, \n2. Perdigón,\n3. Babieca", 1]]

             random.shuffle(preguntes)

             llista=[1,5,7,5,3,7]


             for pregunta in preguntes:
                print(pregunta(0))
    
                for respuesta in preguntes:f
                 print(respuesta(1-3))

try:
    jugadors=int(input("Quantes persones aneu a jugar (2-4)?: "))
    
    if (jugadors == 2):

        ganar = int(3)
        aciertos_j1 = 0
        aciertos_j2 = 0
        
        
    elif (jugadors == 3):

        ganar = int(3)
        aciertos_j1 = 0
        aciertos_j2 = 0
        aciertos_j3 = 0

    elif (jugadors == 4):

        ganar = int(3)
        aciertos_j1 = 0
        aciertos_j2 = 0
        aciertos_j3 = 0
        aciertos_j4 = 0

    else:
        print("Tens que elegir entre 2 i 4 jugadors")

except:
    print("Tens que posar un numero")
