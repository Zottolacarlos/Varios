import psycopg2
from faker import Faker
import random

# Crea una instancia de Faker
faker = Faker()

conn = psycopg2.connect(host="localhost", port=5432, database="localcharly", user="postgres", password="123")
cur = conn.cursor()

# Crea 10 registros aleatorios de usuarios
for i in range(10):
    username = faker.user_name()
    dni = str(random.randint(10000000, 99999999))
    fecha_nacimiento = faker.date_of_birth().strftime('%Y-%m-%d')
    password = 123456

    cur.execute("INSERT INTO usuarios (username, dni, fecha_nacimiento, password) VALUES (%s, %s, %s, %s)", (username, dni, fecha_nacimiento, password))

conn.commit()
cur.close()
conn.close()