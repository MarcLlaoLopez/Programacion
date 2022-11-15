from ossaudiodev import SOUND_MIXER_TREBLE
import re


letras = ("T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E")

DNI=input("Introdueix el teu DNI: ")

resultado = int(DNI[0:8])%23
print(resultado, letras[resultado])

print(bool (DNI[8]==letras[resultado]))

