def cerorepetido(*args):
    i = 0
    for n in args:
        if n == 0:
            i += 1

    if i >= 2:
        print("True")
    else: print("False")
  

cerorepetido(5,4,6,0,9,8,7,0)