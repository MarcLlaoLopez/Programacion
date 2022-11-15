
#El menu ja està implementat
print("Que programa vols fer?:")

print("1. Mitjana aritmetica")
print("2. IMC")
print("3. Calcular Fahrenheid")
print("4. Calcular segons")

try:

    seleccio = int(input("Quin exercici vols fer? (tens que seleccionar un numero entre 1-4): "))

    if (seleccio == "1"):

    #Primer programa

        print("Crea un programa que a partir de dos números et calculi la mitjana aritmètica")
        numero1=int(input("Numero 1: "))
        numero2=int(input("Numero 2: "))

        resultado=(numero1+numero2)/2

        print("Resultado: ",resultado)

    elif (seleccio == "2"):

    #Segon programa

        print("Crea un programa que a partir d’un pes i una altura et calculi l’índex de massa corporal.")

        pes=int(input("El teu pes (en kg) es: "))
        altura=float(input("La teua altura (en m) es: "))

        IMC=(pes/(altura*altura))

        print("El teu IMC es de: ",IMC)

    elif (seleccio == "3"):
    #Tercer programa

        print("Crea un programa que a partir d’una temperatura en Celsius et calculi la temperatura en Fahrenheid.")

        temp=int(input("Disme una temperatura en Celsius: "))

        temp_f = temp * (9/5) + 32

        print("Estem a ",temp_f,"º Fahrenheid")

    elif (seleccio == "4"):

    #Cuart programa

        print("Crea un programa que a partir d’una hora i uns minuts els calculi en segons.")

        hora=int(input("Disme una hora: ")) 
        minuts=int(input("Disme minuts: "))

        segons=(hora * 60 * 60)+(minuts * 60)

        print("Son un total de:",segons,"segons")

    else:
        print("Tens que elegir entre 1-4, no un altra cosa")

except:
    print("Tens que seleccionar un numero")
        