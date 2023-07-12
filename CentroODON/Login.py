import tkinter as tk
import psycopg2

def login():
    # Conexión a la base de datos
    conn = psycopg2.connect(
        host="localhost",
        database="localcharly",
        user="postgres",
        password="123"
    )
    cur = conn.cursor()

    # Verificar si el usuario existe y la contraseña es correcta
    username = username_entry.get()
    password = password_entry.get()
    cur.execute("SELECT username FROM usuarios WHERE username = %s AND password = %s", (username, password))
    result = cur.fetchone()

    # Cerrar la conexión a la base de datos
    cur.close()
    conn.close()

    # Mostrar el resultado en la interfaz gráfica
    if result is not None:
        result_label.config(text="Login exitoso!")
    else:
        result_label.config(text="Nombre de usuario o contraseña incorrecta.")

# Crear la ventana y los widgets
root = tk.Tk()
root.geometry("300x200")

username_label = tk.Label(root, text="Nombre de usuario:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Contraseña:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Ingresar", command=login)
login_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()