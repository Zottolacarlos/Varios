import psycopg2
import sqlite3

conn = psycopg2.connect(
    #host="odonpostgres.proxy-cmvlu04dr0gc.sa-east-1.rds.amazonaws.com",
    host="database-1.cmvlu04dr0gc.sa-east-1.rds.amazonaws.com",
    port=5432,
    dbname="456",
    user="postgres",
    password="macrossSDF1&"
)

cursor = conn.cursor()



# Conexión a la base de datos
#conn = sqlite3.connect('usuarios.db')

# Crear tabla de usuarios
cursor.execute('''CREATE TABLE tipo_usuario
          (nombre_tipousuario VARCHAR(50) NOT NULL,
           tipo_usuario SERIAL PRIMARY KEY); ''')

# Insertar un usuario de ejemplo

# Confirmar cambios en la base de datos
conn.commit()

# Cerrar la conexión
conn.close()

cursor.close()


