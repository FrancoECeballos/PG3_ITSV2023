print("Ejercício 1: \n")

class Persona():
    def setNombre(self, nombre):
        self.nombre = nombre
        print("Nombre definido\n")
    def printNombre(self):
        print("Mi nombre es ", self.nombre, "\n")

p1 = Persona
p1.setNombre(p1, input("Introduce tu nombre: "))
p1.printNombre(p1)


