def palabraporletra(palabra):
    palabra2 = ""
    for m in palabra:
        palabra2 = palabra2+ m + " "

    mipalabralista = palabra2.split()
    mipalabralista.sort()

    palabrafinal = ""
    for j in mipalabralista:
        if j not in palabrafinal:
            palabrafinal = palabrafinal+j

    print(palabrafinal)


palabraporletra("entretenido")
