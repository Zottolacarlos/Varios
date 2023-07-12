import psycopg2
import sqlite3

conn = psycopg2.connect(
    #host="odonpostgres.proxy-cmvlu04dr0gc.sa-east-1.rds.amazonaws.com",
    host="127.0.0.1",
    port=5432,
    database="localcharly",
    user="postgres",
    password="123"
)


cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE usuarios (
        username VARCHAR(50) NOT NULL,
        dni VARCHAR(20) NOT NULL,
        fecha_nacimiento DATE NOT NULL,
        password VARCHAR(100) NOT NULL,
        PRIMARY KEY (dni)
    )
""")

conn.commit()
cursor.close()
conn.close()