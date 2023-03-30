numero = (input("Ingrese un número y veremos si es Step o no: \n"))
lista = []

for i in range(len(numero)):
    lista.append(numero[i])

for i in range(len(lista)):
    if lista[i-1] > lista[i] or lista[i-1] < lista[i]:
        step = True
    else:
        step = False

if step:
    print(numero, " es un número Step.")
else:
    print(numero, " no es un número Step.")