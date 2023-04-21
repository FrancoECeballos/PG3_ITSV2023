import os, pickle
'''print("Ejercicio N°1: \n")

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
        if continuar=="N" or "n":
            break

print("\nEjercicio N°2 y N°4: \n")

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
        if continuar=="N" or "n":
            break

print("\nEjercicio N°3: \n")

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

try:
    mes = int(input("Ingrese el número del mes: "))
    print("\nEl mes ingresado es: ", meses[mes-1])
except IndexError:
    print("Hubo un error en el ingreso de datos. El mes ingresado no existe.")'''

print("\nEjercicio N°5: \n")

strings = ["Este es un string que va a servir de ejemplo.", "Este es otro string que va a servir de ejemplo.", "Este no."]

pickle.dump(strings, open('actividad5', 'wb'))
print(pickle.load(open('actividad5', 'rb')),"\n")

try:
    pickle.dump(1, open('actividad5', 'wb'))
    print(pickle.load(open('actividad5', 'rb')),"\n")
except pickle.UnpicklingError:
    print("Hubo un error en el ingreso de datos. No se puede leer un Entero.")
