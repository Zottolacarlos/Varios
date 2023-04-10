def contar_primos(x):
    i = 0
    primo = []
    for n in range(2,x):

        for j in range(2,n+1):

          if (n % j) == 0:
            i += 1

        if i > 1:
            pass
        else: primo.append(n)

        i = 0

    print(primo)

contar_primos(8)