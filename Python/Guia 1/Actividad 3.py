caracter = input("Ingrese un caracter y haremos un rectangulo con el: \n")
alto = int(input("Ingrese el alto del rectangulo: \n"))
ancho = int(input("Ingrese el ancho del rectangulo: \n"))

for i in range(alto):
    for j in range(ancho):
        print(caracter, end="")
    print()
