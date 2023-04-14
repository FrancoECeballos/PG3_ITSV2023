print("Ejercicio N°1: \n")

while True:
    try:
        num1=int(input("Ingrese un numero: "))
        num2=int(input("Ingrese otro numero: "))
        suma= num1 + num2
        print("\nEl resultado es: ", suma)
    except ValueError:
        print("\nHubo un error en el ingreso de datos. El dato ingresado no es un múmero")
    finally:
        continuar=input("¿Desea continuar? Si desea detener el programa, ingrese 'N': \n")
        if continuar=="N" or continuar=="n":
            break

print("\nEjercicio N°2: \n")

while True:
    try:
        num1=int(input("Ingrese un numero: "))
        num2=int(input("Ingrese otro numero: "))
        division= num1 / num2
        print("\nEl resultado es: ", division)
    except ValueError:
        print("\nHubo un error en el ingreso de datos. El dato ingresado no es un múmero")
    except ZeroDivisionError:
        print("\nHubo un error en el ingreso de datos. No se puede dividir por 0")
    finally:
        continuar=input("¿Desea continuar? Si desea detener el programa, ingrese 'N': \n")
        if continuar=="N" or continuar=="n":
            break