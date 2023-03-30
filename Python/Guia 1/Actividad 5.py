igual = 0
j = 0
texto = input("Este programa le dira si su palabra es un Palíndromo (capicula). Ingrese la palabra que desea evaluar: \n")

for i in reversed(range(0, len(texto))):
    if texto[i].lower() == texto[j].lower():
        igual += 1
    j += 1

if len(texto) == igual:
    print("La frase ingresada es palindromo")
else:
    print("La frase ingresada no es palindromo")