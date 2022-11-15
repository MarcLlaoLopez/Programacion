#Crea un programa que a partir d'una cadena de 4 caràcters (numèrics) preguntada a l'usuari, (com "123456") imprimeixi la suma dels números que la formen. Teniu en compte que només s'ha d'utilitzar un input, estem treballant les cadenes.



print("Escriu 4 caracters numerics");
cadena=input();
resultat=(int(cadena[0]))+(int(cadena[1]))+(int(cadena[2]))+(int(cadena[3]));
print(resultat);

#Consulta els mètodes "built-in" que teniu disponibles per a cadenes i crea un programa que a partir d'una frase donada per l'usuari calculi:


from re import X

print("Escriut una frase");
text = input();

#Número de caràcters.

caracter = len(text);

print("La teua frase te",caracter ,"caracters");

#Número de paraules.

paraula = len(text.split());

print("La teua frase te",paraula ,"paraules");

#Frase  amb totes les paraules en majúscula.

mayuscula = text.upper();

print(mayuscula);

#Frase  amb totes les paraules en minúscula.

minuscula = text.lower();

print(minuscula);

#Preguntat un caràcter a l'usuari retorni la posició de la primera coincidència trobada a la frase.

##caracter1 = input;
##print("Elegix un caracter:",caracter1)
##print(text.find(caracter1))


#Preguntat un caràcter a l'usuari retorni la posició de la darrera coincidència trobada a la frase.

#Preguntat un caràcter a l'usuari retorni el número de coincidències trobades a la frase.

#Mostri el número de vocals del text (has d'optimitzar al màxim aquest codi!!).


numero1 =str(text.count("a"))
numero2 =str(text.count("e"))
numero3 =str(text.count("i"))
numero4 =str(text.count("o"))
numero5 =str(text.count("u"))

print("Hi ha",numero1 ,"a")
print("Hi ha",numero2 ,"e")
print("Hi ha",numero3 ,"i")
print("Hi ha",numero4 ,"o")
print("Hi ha",numero5 ,"u")


#Modifica el primer programa per a que abans de donar el resultat mostri si és cert que la cadena només conté números.
