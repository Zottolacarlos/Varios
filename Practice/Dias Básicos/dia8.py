def vidas():
    x = 4
    while x > 0:
        x -= 1
        yield x


perder_vida = vidas()
x = 4
while x > 0:
    x = next(perder_vida)
    match x:
        case x if x == 3:
            print("Te quedan 3 vidas")

        case 2:
            print("Te quedan 2 vidas")

        case 1:
            print("Te queda 1 vida")

        case _:
            print("Game Over")