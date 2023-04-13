# Aumento de datos con ImageDataGenerator
import keras
import tensorflow
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from keras.preprocessing.image import ImageDataGenerator
import numpy as np

# Crear el dataset generador
datagen = ImageDataGenerator(
    rescale=1. / 255,
    rotation_range=30,
    width_shift_range=0.25,
    height_shift_range=0.25,
    shear_range=15,
    zoom_range=[0.5, 1.5],
    validation_split=0.2  # 20% para pruebas
)

# Generadores para sets de entrenamiento y pruebas
data_gen_ent = datagen.flow_from_directory('dataset', target_size=(224, 224),
                                           batch_size=32, shuffle=True, subset='training')
data_gen_pruebas = datagen.flow_from_directory('dataset', target_size=(224, 224),
                                               batch_size=32, shuffle=True, subset='validation')

# Imprimir 10 imagenes del generador de entrenamiento
"""for imagen, etiqueta in data_gen_ent:
    for i in range(10):
        plt.subplot(2, 5, i+1)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(imagen[i])
    break

plt.show()"""

import tensorflow as tf
import tensorflow_hub as hub

url = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4"
mobilenetv2 = hub.KerasLayer(url, input_shape=(224, 224, 3))

# Congelar el modelo descargado
mobilenetv2.trainable = False

modelo = tf.keras.Sequential([
    mobilenetv2,
    tf.keras.layers.Dense(3, activation='softmax')
])
modelo.summary()

# Compilar como siempre
modelo.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)
# Entrenar el modelo
EPOCAS = 50

historial = modelo.fit(
    data_gen_ent, epochs=EPOCAS, batch_size=32,
    validation_data=data_gen_pruebas
)
# Graficas de precisión
"""acc = historial.history['accuracy']
val_acc = historial.history['val_accuracy']

loss = historial.history['loss']
val_loss = historial.history['val_loss']

rango_epocas = range(50)

plt.figure(figsize=(8,8))
plt.subplot(1,2,1)
plt.plot(rango_epocas, acc, label='Precisión Entrenamiento')
plt.plot(rango_epocas, val_acc, label='Precisión Pruebas')
plt.legend(loc='lower right')
plt.title('Precisión de entrenamiento y pruebas')

plt.subplot(1,2,2)
plt.plot(rango_epocas, loss, label='Pérdida de entrenamiento')
plt.plot(rango_epocas, val_loss, label='Pérdida de pruebas')
plt.legend(loc='upper right')
plt.title('Pérdida de entrenamiento y pruebas')
plt.show()"""

#Categorizar una imagen de internet
from PIL import Image
import requests
from io import BytesIO
import cv2
from PIL import Image

def categorizar(url):
  respuesta = requests.get(url)
  img = Image.open(BytesIO(respuesta.content))
  img = np.array(img).astype(float)/255

  img = cv2.resize(img, (224,224))

  prediccion = modelo.predict(img.reshape(-1, 224, 224, 3))

  return np.argmax(prediccion[0], axis=-1)

# 0 = cuchara, 1 = cuchillo, 2 = tenedor
url = 'https://media.wonderfulhomeshop.com/c/product/cuchara-cafe-alida-comas-520x520.jpg' #debe ser 2
prediccion = categorizar(url)
print(prediccion)

"""#Crear la carpeta para exportarla a TF Serving
!mkdir -p carpeta_salida/modelo_cocina/1

#Guardar el modelo en formato SavedModel
modelo.save('carpeta_salida/modelo_cocina/1')

!zip -r modelo_cocina.zip /content/carpeta_salida/modelo_cocina/"""