año = int(input("Ingrese un año y le diremos si es bisiesto o no: \n"))

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print("El año ", año, "es bisiesto.")
        else:
            print("El año ", año, " no es bisiesto.")
    else:
        print("El año ", año, "es bisiesto.")
else:
    print("El año ", año, "no es bisiesto.")