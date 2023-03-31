print("Ejercício 1: \n")

class Persona():
    def setNombre(self, nombre):
        self.nombre = nombre
        print("Nombre definido\n")
    def printNombre(self):
        print("Mi nombre es", self.nombre, "\n")

p1 = Persona
p1.setNombre(p1, input("Introduce tu nombre: "))
p1.printNombre(p1)

print("Ejercício 2: \n")

class Alumno():
    def checkNota(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        if nota >= 6:
            print("\nEl alumno", nombre, "aprobo la materia \n")
        else:
            print("\nEl alumno", nombre, "reprobo la materia \n")


alumno1 = Alumno()
alumno2 = Alumno()

alumno1.checkNota(input("Introduce el nombre del alumno 1: "), int(input("Introduce la nota del alumno 1: ")))
alumno2.checkNota(input("Introduce el nombre del alumno 2: "), int(input("Introduce la nota del alumno 2: ")))#/

print("Ejercício 3: \n")

class Triangulo():
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    def ladoMayor(self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print("\nEl lado mayor es", self.lado1, "\n")
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            print("\nEl lado mayor es", self.lado2, "\n")
        elif self.lado3 > self.lado1 and self.lado3 > self.lado2:
            print("\nEl lado mayor es", self.lado3, "\n")
        else:
            print("\nNo hay un solo lado que sea mayor que el resto\n")
    def tipoTriangulo(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("Es un triángulo equilátero\n")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("Es un triángulo isósceles\n")
        else:
            print("Es un triángulo escaleno\n")

triangulo1 = Triangulo(int(input("Introduce el lado 1: ")), int(input("Introduce el lado 2: ")), int(input("Introduce el lado 3: ")))
triangulo1.ladoMayor()
triangulo1.tipoTriangulo()