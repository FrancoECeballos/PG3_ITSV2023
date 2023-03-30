lista = []
i = 0

while i != 7:
    numero = int(input("Por favor ingrese 7 números para crear una lista que luego será ordenada: \n" ))
    lista.append(numero)
    i = i + 1

for i in range(len(lista)-1):
    for j in range(len(lista)-1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print("Lista de números: ", lista)