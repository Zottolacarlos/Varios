#juego de adivinar el numero
from random import *
objetivo = randint(1,101)
jugador = input("Jugador Ingresa tu Nombre: ")
intento = 1
print(f"Bueno {jugador} he pensado un numero entre 1 y 100, crees que puede adivinarlo?")

while input("Intentar resolver el Acertijo (ingrese si o no): ") != "no":
    while intento <= 8:
        x = int(input(f"Ingresar el Intento {intento}: "))
        match x:
            case x if x < 1:
                print(f"El numero {x} NO está permitido")
            case x if x > 100:
                print(f"El numero {x} NO está permitido")
            case x if x < objetivo:
                print(f"El numero {x} es MENOR al numero que pensé")
            case x if x > objetivo:
                print(f"El numero {x} es MAYOR al numero que pensé")
            case x if x == objetivo:
                print("ACERTASTE!! FELICITACIONES!!")
                break
            case _:
                pass
        intento += 1
    else:
        print("SE TE ACABARON LOS INTENTOS")
        print(f"El numero que habia pensado es el: {objetivo}")
        print("MEJOR SUERTE LA PROXIMA")
else:
    print("ADIOS")
