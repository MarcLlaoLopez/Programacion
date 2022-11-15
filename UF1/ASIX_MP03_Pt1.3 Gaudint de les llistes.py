#Crea un programa que demani una cadena de 4 caràcters (numèrics) a l'usuari, (com "1234") els emmagatzemi a una llista convertits en enters i imprimeixi la suma dels números que la formen.

print("Escriu cuatre caracters:")

caracter = input()

caracters = [int(caracter[0]), int(caracter[1]), int(caracter[2]), int(caracter[3])]

resultat=(sum(caracters));

print(resultat);

#Demana a l'usuari un número i afegeix-lo al final de la llista amb un mètode de llista.

print("Dime un numero: ")

caracters.append(int(input()))


print(caracters)

#Ara elimina aquest número de la llista amb un mètode de llista.


caracters.pop()

print(caracters)

#Ordena la llista amb un mètode de llista.

print("Ahora ordenamos la lista: ")

caracters.sort()

print(caracters)


#Mostra el seu número màxim i el seu mínim, extrets amb funcions internes.

print(max(caracters), "es el numero maximo")

print(min(caracters), "es el numero minimo")


#Calcula la mitjana aritmètica de la llista a partir de les funcions internes sum() i len().

media = int(sum(caracters)) / int(len(caracters))

print( media, "es la media de caracters")