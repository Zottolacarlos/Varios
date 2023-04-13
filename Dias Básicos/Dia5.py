from random import choice

def pedirletra():
     letra = input("Ingrese una Letra: ")
     return letra

def modificalista(listaobjetivo,letra,*args):
          #print(args)
          for n in args:
              # print(n)
               listaobjetivo[n] = letra
          return listaobjetivo


def buscarletra(palabraobjetivo,tamaniopalabra,vidas,listaobjetivo):
     b = 0
     letra = pedirletra()
     if letra in palabraobjetivo:
          print("Acertó una letra!")
          index = palabraobjetivo.find(letra)
          index2 = palabraobjetivo.find(letra,index+1,len(palabraobjetivo))
          #print(listaobjetivo)
          if index2 > 0:
               print(f"Palabra secreta: {modificalista(listaobjetivo, letra, index,index2)}")
               return 2
          else:
               print(f"Palabra secreta: {modificalista(listaobjetivo, letra, index)}")
               return 1
          print("------------------------------------------------------")

     else:
          print("La letra ingresada no pertenece a la palabra secreta")
          print(f"Palabra secreta: {listaobjetivo}")
          print("------------------------------------------------------")
          return 0

def ganajuego(tamaniopalabra,resultadodef):
     tamaniopalabra = tamaniopalabra - resultadodef
     return tamaniopalabra


def juego():
     listaobjetivo = []
     palabraobjetivo = "etcetera"
     tamaniopalabra = len(palabraobjetivo)
     vidas = 6
     for m in palabraobjetivo:
          listaobjetivo.append("-")

     while vidas > 0:
          resultadoletra = buscarletra(palabraobjetivo,tamaniopalabra,vidas,listaobjetivo)
          if resultadoletra == 0:
               vidas -= 1
               print(f"Le quedan {vidas} vidas")
               print("------------------------------------------------------")
              # print("\n")

          else:
               tamaniopalabra = ganajuego(tamaniopalabra,resultadoletra)
               if tamaniopalabra == 0:
                    print("\nGANO EL JUEGO!!")
                    print("\o/ \o/ \o/ \o/")
                    break

     if vidas <= 0:
          print("\n \n Perdió el juego! xC")


juego()