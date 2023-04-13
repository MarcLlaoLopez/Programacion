import subprocess

# Ejecutar el comando nmap -sV y almacenar la salida en una variable
output = subprocess.run(["nmap", "-sV", "192.168.88.224"], capture_output=True, text=True)

# Separar la salida en líneas
lines = output.stdout.split("\n")

# Iterar sobre las líneas de la salida
for line in lines:
    # Buscar líneas que contengan información sobre el puerto y la versión del servicio
    if "open" in line:
        # Imprimir el puerto y la versión del servicio
        print(line)