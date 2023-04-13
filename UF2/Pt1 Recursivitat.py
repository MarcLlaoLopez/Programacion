#Crea una funció recursiva que calculi el factorial d’un número donat. Recorda el factorial de 5: 5! = 1*2*3*4*5

def factorial(n):
 
 if n == 1:
    return 1
 else:
    return n * factorial(n - 1)
 

numero = int(input("Elige un numero: "))
print(factorial(numero))

#Crea una funció recursiva que donat un número natural en calculi la seva conversió a binari. Pe: binari(6) = “110”

def binari(b):
    if b == 0:
       return 0
    else:
       return b % 2 + 10 *binari(b//2)

num_b = int(input("Elige un numero para convertir a binario: "))
print(binari(num_b))

#Modifica la funció anterior per a que accepti qualsevol tipus de base de 2 a 10 Pe: conversioBase(15, 8) = “17”

def conversioBase(n, base):
   if n == 0:
      return 0
   
   elif n < base:
      return str(n)
   
   else:
      return conversioBase(n // base, base) + str(n % base)

num1 = int(input("Dime un numero: "))
num2 = int(input("Dime otro numero: "))
print(conversioBase(num1,num2))   

#Crea una funció recursiva que donat un array de número naturals en trobi el màxim. Prohibit utilitzar funcions integrades del python!

def n_maxim(arr):
    if len(arr) == 1:
        return arr[0]
    
    max_of_rest = n_maxim(arr[1:])
    if arr[0] > max_of_rest:
        return arr[0]
    else:
        return max_of_rest


numeros = input("Dime un total de 4 numeros separados por un espacio ('Ejemplo: 1 2 3 4'): ")
l_numeros=numeros.split()
print(n_maxim(l_numeros))
