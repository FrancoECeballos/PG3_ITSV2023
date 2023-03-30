vocales = ["a", "e", "i", "o" ,"u", "A", "E", "I", "O", "U"]
frase = str(input("Ingrese una frase para que el programa cuente sus vocales: \n"))
contador = 0

for i in range(len(frase)):
    if frase[i] in vocales:
        contador = contador + 1

print("Su frase tiene ", contador, "vocales.")