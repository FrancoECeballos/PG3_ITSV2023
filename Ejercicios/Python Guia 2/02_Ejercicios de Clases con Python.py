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
alumno2.checkNota(input("Introduce el nombre del alumno 2: "), int(input("Introduce la nota del alumno 2: ")))
