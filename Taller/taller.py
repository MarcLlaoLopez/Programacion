#pip3 install pyqrcode
import pyqrcode
#pip3 install pypng
import png

#Cadena a convertir
s="https://matias.ma/nsfw/"

url=pyqrcode.create(s)

print(url.terminal())

url.png('elmeuqr.png', scale = 6)
