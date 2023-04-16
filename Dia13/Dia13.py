import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# escuchar nuestro microfono y devolver el audio como texto
def transform_audio_texto():
    """almacenar reconocerdor"""
    r = sr.Recognizer()

    """mic_list = sr.Microphone.list_microphone_names()
    print("Lista de micrófonos disponibles:")
    for i, microphone_name in enumerate(mic_list):
        print(f"{i}: {microphone_name}")"""

    with sr.Microphone() as origen:
        # tiempo de espera
        r.pause_threshold = 0.8
        print("Ya PUEDES HABLAR:")

        audio = r.listen(origen)

        try:
            ##buscar en google lo q haya escuchado
            pedido = r.recognize_google(audio, language="es-ar")

            # imprimir de que pudo ingresar
            print("Dijiste:" + pedido)

        except sr.UnknownValueError:
            # prueba de q no comprenio el audio
            print("Ups no entendi")
            return "Sigo esperando1"

        except sr.RequestError:
            print("Ups no hay servicio")
            return "Sigo Esperando2"

        except:
            print("Ups algo salio mal")
            return "Sigo Esperando3"

            return pedido


# funcion para q el asistente pueda ser escuchado
def hablar(mensaje):
    # encender el motor pyttsx3
    engine = pyttsx3.init()

    engine.say(mensaje)
    engine.runAndWait()


hablar(transform_audio_texto())
