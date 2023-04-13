import os
from zipfile import ZipFile
#Crear las carpetas para subir las imagenes
try:
    os.mkdir('cuchillos')
except OSError as error:
    print(error)

try:
    os.mkdir('tenedores')
except OSError as error:
    print(error)
try:
    os.mkdir('cucharas')
except OSError as error:
    print(error)

dir_actual = os.getcwd()
os.chdir('cuchillos')
with ZipFile('cuchillos.zip', 'r') as zobject:
    zobject.extractall()

os.chdir(dir_actual)
os.chdir('cucharas')
with ZipFile('cucharas.zip', 'r') as zobject:
    zobject.extractall()

os.chdir(dir_actual)
os.chdir('tenedores')
with ZipFile('tenedores.zip', 'r') as zobject:
    zobject.extractall()
