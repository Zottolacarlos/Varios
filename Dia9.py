import re


def verificar_saludo(frase):
    patron = r'^Hola'

    resultado = re.search(patron, frase)

    if resultado:
        print("Ok")

    else:
        print("No has saludado")


verificar_saludo('Hola sadfsdf')