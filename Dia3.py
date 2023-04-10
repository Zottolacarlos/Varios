texto = input("Ingresar un texto: ").lower()
a = input("ahora ingresa 3 palabras: ").lower()
b = input().lower()
c = input().lower()

resultado = texto.count(a)
resultado2 = texto.count(b)
resultado3 = texto.count(c)

textolista = texto.split()
print(textolista)
resultado4 = str(len(textolista))
textolista.reverse()

textoalainversa = " ".join(textolista)


print(f"De la primera letra existen {resultado} ocurrencias")
print(f"De la segunda letra existen {resultado2} ocurrencias")
print(f"De la tercera letra existen {resultado3} ocurrencias")

print("El total de palabras en la frase ingresa es de "+ resultado4)

print(f"La primera letra del texto es: {texto[0]} y la ultima es {texto[-1]}")
print(f"El texto al reves quedaría {textoalainversa}")
lacondicion = 'python' in texto
dic = {True:"si",False:"no"}

print(f"La palabra 'Python' {dic[lacondicion]} se encuentra en el texto proporcionado")

