# Codi fet per Yassin Bekkaoui i per Marc Llao

import netifaces
import subprocess

# Obtener información sobre todas las interfaces de red disponibles
interfaces = netifaces.interfaces()

# Crear un diccionario para almacenar las direcciones IP de las interfaces
ips = {}

# Recorrer todas las interfaces y obtener su dirección IP
for interface in interfaces:
    # Obtener información de la interfaz
    info = netifaces.ifaddresses(interface)

    # Verificar si la interfaz tiene una dirección IP asignada
    if netifaces.AF_INET in info:
        # Obtener la dirección IP y almacenarla en el diccionario
        ips[interface] = info[netifaces.AF_INET][0]['addr']

# Imprimir el diccionario con las direcciones IP de las interfaces

contador= 1
lista= []

for interfaz in ips:
    
    print(contador, '.' ,interfaz)
    contador+=1
    lista.append(ips[interfaz])



seleccion = int(input("Quina interficie vols fer-li un nmap sweap:\n"))

redes = (subprocess.run(["nmap", lista[seleccion-1] + "/24", "-n", "-sP"], capture_output=True, text=True))

redes = redes.stdout.split("\n")


redes2 = []

for linia in redes:
    if linia[:1] == "N":
        redes2.append(linia.split(" ")[-1])

print("Elige la ip que quieres escanear: ")      
num=1

del redes2[-1]


for red in redes2:
    
    print(str(num)+": "+str(red))
    num+=1

escaneo = int(input("Que IP quieres escanear? \n"))

vport = subprocess.run(["nmap", "-sV", str(redes2[escaneo-1])], capture_output=True, text=True)

vport = vport.stdout.split("\n")

vport2 = []
vport2_version = []
dicc_vport2 = {}

for i in range(len(vport)):
        if "open" in (vport[i]):
            vport[i].split()
            vport2.append(vport[i][:7])   
            vport2_version.append(vport[i][21:]) 
        else:
            continue

elementos = 0
while elementos <= len(vport2):
    dicc_vport2[vport2[elementos]] = vport2_version[elementos]
    elementos += 1
print(dicc_vport2)

puertos = {}
