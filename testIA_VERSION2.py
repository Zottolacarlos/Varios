import tensorflow as tf
import numpy as np

lottery_data = np.loadtxt("lottery_data.csv", delimiter=",", skiprows=1, dtype=str)

# Convertir la columna "resultados" en una matriz NumPy de enteros
results = np.array([row.split(" ") for row in lottery_data[:, 1]], dtype=int)

# Divide los datos en conjuntos de entrenamiento y validación
train_data = lottery_data[:800]
val_data = lottery_data[800:]


# Transformar los datos en secuencias de longitud window_size+1
# Define una función para crear secuencias de entrada y salida
def create_sequences(values, window_size, time_steps=5):
    x = []
    y = []
    for i in range(len(values)-time_steps):
        x.append(values[i:i+time_steps])
        y.append(values[i+time_steps])
    return np.array(x), np.array(y)

# Crea las secuencias de entrada y salida
train_data, train_labels = create_sequences(lottery_data[:800,0], window_size=5)
val_data, val_labels = create_sequences(lottery_data[800:,0], window_size=5)

# Ajusta la forma de los datos de entrada y salida para el modelo LSTM
train_data = np.expand_dims(train_data, axis=2)
val_data = np.expand_dims(val_data, axis=2)

# Define los parámetros del modelo
num_features = 1
hidden_units = 64

# Define el modelo LSTM
model = tf.keras.Sequential([
  tf.keras.layers.LSTM(hidden_units, input_shape=(None, num_features)),
  tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse')

history = model.fit(train_data, train_labels, epochs=50, validation_data=(val_data, val_labels))

test_data = lottery_data[800:,0]
test_data = test_data.reshape((test_data.shape[0], 5, 1))
predictions = model.predict(test_data)

# Evalúa la precisión del modelo
accuracy = np.mean(np.abs(predictions - lottery_data[800:,0]))
print(f"La precisión del modelo es del {100-accuracy*100}%")


