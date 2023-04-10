import DarNumeros
from os import system

def turnero():
    elija = ''

    while elija != 'x':

        print("""Bienvenido, elija su Destino:
            [c]Cosmeticos
            [f]Farmacia
            [p]Perfumeria
            [x]Salir""")
        try:
            elija = input("Su Elección: ").lower()
            ['c', 'f', 'p', 'x'].index(elija)
        except ValueError:
            print("No es una opcion válida")

        else:
            if elija != 'x':
                DarNumeros.decoracion(elija)




    else:
        print("Adios")

turnero()