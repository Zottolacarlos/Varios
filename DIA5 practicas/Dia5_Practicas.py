def devolver_distintos(*args):
    total = 0
    i = 0
    i = args[0] #es el mayor
    j = args[0] #es el menor
    k = args[0] #esel del medio
   # print(i,j,k)
    for n in args:
         match n:
            case n if n > i:
                    i = n
                    total += n
            case n if n < j:
                    j = n
                    total += n
            case n if j < n < i:
                    k = n
                    total += n
            case _:
                 total += n
    print(f"TOTAL ES {total}")

    match total:
        case total if total > 15:
                       print(i)
        case total if total < 10:
                      print(j)
        case total if 10 <= total <= 15:
                        print(k)
        case _:
             pass


devolver_distintos(4,3,6)