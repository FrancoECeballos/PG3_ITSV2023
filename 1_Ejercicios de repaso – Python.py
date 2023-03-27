def ej1(numero):
    lista = [2, 4, 8, 12, 14, 16, 20, 7, 11, 1]
    truers = False

    for i in range(len(lista)):
        if lista[i] == numero:
            print("El número se encuentra en la posición ", i)
            truers = True
    if not truers:
        print("El número no se encuentra en la lista")
    print("Lista de números: ", lista, "\n")

def ej2(año):
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                print("El año ", año, "es bisiesto.\n")
            else:
                print("El año ", año, " no es bisiesto.\n")
        else:
            print("El año ", año, "es bisiesto.\n")
    else:
        print("El año ", año, "no es bisiesto.\n")

def ej3(caracter,alto,ancho):
    for i in range(alto):
        for j in range(ancho):
            print(caracter, end="")
        print()

def ej3desafio(caracter,filas):
    k = 0

    for i in range(1, filas + 1):
        for space in range(1, (filas - i) + 1):
            print(end="  ")

        while k != (2 * i - 1):
            print(caracter, end=" ")
            k += 1

        k = 0
        print()

def ej4(numero1,numero2,numero3,numero4,numero5,numero6,numero7):
    lista = []
    i = 0

    lista.append(numero1)
    lista.append(numero2)
    lista.append(numero3)
    lista.append(numero4)
    lista.append(numero5)
    lista.append(numero6)
    lista.append(numero7)

    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    print("Lista de números: ", lista, "\n")

def ej5(texto):
    igual = 0
    j = 0

    for i in reversed(range(0, len(texto))):
        if texto[i].lower() == texto[j].lower():
            igual += 1
        j += 1

    if len(texto) == igual:
        print("La frase ingresada es palindromo. \n")
    else:
        print("La frase ingresada no es palindromo. \n")

def ej6(frase):
    vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    contador = 0

    for i in range(len(frase)):
        if frase[i] in vocales:
            contador = contador + 1

    print("Su frase tiene ", contador, "vocales.\n")

def ej7(numero):
    lista = []

    for i in range(len(numero)):
        lista.append(numero[i])

    for i in range(len(lista)):
        if lista[i - 1] > lista[i] or lista[i - 1] < lista[i]:
            step = True
        else:
            step = False

    if step:
        print(numero, " es un número Step.\n")
    else:
        print(numero, " no es un número Step.\n")

print("Ejercicio 1: \n")
ej1(int(input("Ingrese un número y le diremos si esta o no en la lista: \n")))
print("Ejercicio 2: \n")
ej2(int(input("Ingrese un año y le diremos si es bisiesto o no: \n")))
print("Ejercicio 3: \n")
ej3(input("Ingrese un caracter y haremos un rectangulo con el: \n"),int(input("Ingrese el alto del rectangulo: \n")),int(input("Ingrese el ancho del rectangulo: \n")))
print("Ejercicio 3 (Desafio): \n")
ej3desafio(input("Ingrese un caracter y haremos un triángulo con el: \n"),int(input("Ingrese la cantidad de filas del triánguo: \n")))
print("Ejercicio 4: \n")
ej4(int(input("Por favor ingrese 7 números para crear una lista que luego será ordenada: (0/7)\n")),int(input("Por favor ingrese 7 números para crear una lista que luego será ordenada: (1/7)\n")),int(input("Por favor ingrese 7 números para crear una lista que luego será ordenada: (2/7)\n")),int(input("Por favor ingrese 7 números para crear una lista que luego será ordenada: (3/7)\n")),int(input("Por favor ingrese 7 números para crear una lista que luego será ordenada: (4/7)\n")),int(input("Por favor ingrese 7 números para crear una lista que luego será ordenada: (5/7)\n")),int(input("Por favor ingrese 7 números para crear una lista que luego será ordenada: (6/7)\n")))
print("Ejercicio 5: \n")
ej5(input("Este programa le dira si su palabra es un Palíndromo (capicula). Ingrese la palabra que desea evaluar: \n"))
print("Ejercicio 6: \n")
ej6(str(input("Ingrese una frase para que el programa cuente sus vocales: \n")))
print("Ejercicio 7: \n")
ej7(input("Ingrese un número y veremos si es Step o no: \n"))
