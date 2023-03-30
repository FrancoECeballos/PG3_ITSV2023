caracter = input("Ingrese un caracter y haremos un triángulo con el: \n")
filas = int(input("Ingrese la cantidad de filas del triánguo: \n"))
k = 0

for i in range(1, filas + 1):
    for space in range(1, (filas - i) + 1):
        print(end="  ")

    while k != (2 * i - 1):
        print(caracter, end=" ")
        k += 1

    k = 0
    print()