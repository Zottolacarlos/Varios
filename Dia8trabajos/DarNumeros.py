def darnumero():
    """
    #encargado de dar numeros
    :param categoria: string
    :return: numero
    """

    for x in range(1, 9999):
         yield x


turno = darnumero()

def decoracion(categoria):

    print("*************")
    print("SU NUMERO ES:")
    print(f"C-{next(turno)}")
    print("*************")