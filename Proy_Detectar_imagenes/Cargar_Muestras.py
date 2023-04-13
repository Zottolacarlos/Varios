import os
from zipfile import ZipFile
from os import path
import pathlib



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
"""os.chdir('cuchillos')
with ZipFile('cuchillos.zip', 'r') as zobject:
    zobject.extractall()

os.chdir(dir_actual)
os.chdir('cucharas')
with ZipFile('cucharas.zip', 'r') as zobject:
    zobject.extractall()

os.chdir(dir_actual)
os.chdir('tenedores')
with ZipFile('tenedores.zip', 'r') as zobject:
    zobject.extractall()"""

"""os.chdir(dir_actual)
os.chdir('cucharas')
os.remove('cucharas.zip')
os.chdir(dir_actual)
os.chdir('cuchillos')
os.remove('cuchillos.zip')
os.chdir(dir_actual)
os.chdir('tenedores')
os.remove('tenedores.zip')"""

"""p = pathlib.Path('tenedores/tenedores')
x = 0
for f in p.iterdir():
    x += 1
print(x)

dir_actual = os.getcwd()
p = pathlib.Path('cucharas/cucharas')
x = 0
for f in p.iterdir():
    x += 1
print(x)

dir_actual = os.getcwd()
p = pathlib.Path('cuchillos/cuchillos')

x = 0
for f in p.iterdir():
    x += 1
print(x)"""

maximo = 168
#print(dir_actual)
import numpy as np



#Mostrar algunas imagenes con pyplot
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

plt.figure(figsize=(15,15))

carpeta = 'cuchillos/cuchillos'
imagenes = os.listdir(carpeta)
# print(carpeta)
for i, nombreimg in enumerate(imagenes[:25]):
  # print(nombreimg)
  plt.subplot(5,5,i+1)
  imagen = mpimg.imread(carpeta + '/' + nombreimg)

  plt.imshow(imagen)
  plt.pause(0.5)
  plt.draw()

"""try:
    os.mkdir('dataset')
except OSError as error:
    print(error)

try:
    os.mkdir('dataset/cuchillos')
except OSError as error:
    print(error)

try:
    os.mkdir('dataset/tenedores')
except OSError as error:
    print(error)
try:
    os.mkdir('dataset/cucharas')
except OSError as error:
    print(error)"""

import shutil
"""carpeta_fuente = 'cuchillos/cuchillos'
carpeta_destino = 'dataset/cuchillos'
imagenes = os.listdir(carpeta_fuente)
for i, nombreimg in enumerate(imagenes):
  if i < maximo:
    #Copia de la carpeta fuente a la destino
    shutil.copy(carpeta_fuente + '/' + nombreimg, carpeta_destino + '/' + nombreimg)"""

"""carpeta_fuente = 'cucharas/cucharas'
carpeta_destino = 'dataset/cucharas'
imagenes = os.listdir(carpeta_fuente)

for i, nombreimg in enumerate(imagenes):
  if i < maximo:
    #Copia de la carpeta fuente a la destino
    shutil.copy(carpeta_fuente + '/' + nombreimg, carpeta_destino + '/' + nombreimg)

carpeta_fuente = 'tenedores/tenedores'
carpeta_destino = 'dataset/tenedores'

imagenes = os.listdir(carpeta_fuente)

for i, nombreimg in enumerate(imagenes):
  if i < maximo:
    #Copia de la carpeta fuente a la destino
    shutil.copy(carpeta_fuente + '/' + nombreimg, carpeta_destino + '/' + nombreimg)"""