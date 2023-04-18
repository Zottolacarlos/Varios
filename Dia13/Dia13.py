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
        # print("Ya PUEDES HABLAR:")

        audio = r.listen(origen)

        try:
            ##buscar en google lo q haya escuchado
            pedido = r.recognize_google(audio, language="es-ar")
            return pedido
            # imprimir de que pudo ingresar
            #print("Dijiste:" + pedido)

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



# funcion para q el asistente pueda ser escuchado
def hablar(mensaje):
    # encender el motor pyttsx3
    engine = pyttsx3.init()
    engine.say(mensaje)
    engine.runAndWait()

def pedir_dia():
    dia = datetime.date.today()
    print(dia)
    dia_semana = dia.weekday()
    print(type(dia_semana))
    # crear para los dias
    dia_nombre = {0:'Lunes', 1:'Martes', 2:'Miércoles',3:'Jueves', 4:'Viernes', 5:'Sábado',6:'Domingo'}
    #decir el dia
    hablar(f'Hoy es: {dia_nombre[dia_semana]}')

def pedir_hora():
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos'
    print(hora)
    hablar(hora)

def saludo_inicial():
    hablar("Hola, soy tu Asistente Virtual. Por favor, dime en que te puedo ayudar")

def pedir_cosas():

    saludo_inicial()
    comenzar = True
    while comenzar:
        pedido = transform_audio_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Abriendo YOUTUBE')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Abriendo Navegador')
            webbrowser.open('https://www.google.com')
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL',
                       'amazon': 'AMZN',
                       'google': 'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar("Perdón pero no la he encontrado")
                continue
        elif 'adiós' in pedido:
            hablar("Me voy a descansar, cualquier cosa me avisas")
            break

pedir_cosas()

#hablar()
#pedir_dia()
#pedir_hora()