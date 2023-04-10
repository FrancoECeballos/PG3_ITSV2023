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

print("Ejercício 4: \n")

class Operaciones():
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()
    def suma(self):
        print("\nLa suma de sus números es", self.num1 + self.num2)
    def resta(self):
        print("\nLa resta de sus números es", self.num1 - self.num2)
    def multiplicacion(self):
        print("\nLa multiplicación de sus números es", self.num1 * self.num2)
    def division(self):
        print("\nLa división de sus números es", self.num1 / self.num2, "\n")

operacion = Operaciones(int(input("Introduce el primer número: ")), int(input("Introduce el segundo número: ")))

print("Ejercício 5: \n")

class Persona():
    def setNombre(self, nombre):
        self.nombre = nombre
    def setEdad(self, edad):
        self.edad = edad

class Empleado(Persona):
    def setSalario(self, salario):
        self.salario = salario


p1 = Persona
p1.setNombre(p1, input("Introduce tu nombre: "))
p1.setEdad(p1, int(input("Introduce tu edad: ")))

print("\nNombre:", p1.nombre, "\nEdad:", p1.edad, "\n")

e1 = Empleado
e1.setNombre(e1, input("Introduce el nombre de tu empleado: "))
e1.setEdad(e1, int(input("Introduce la edad de tu empleado: ")))
e1.setSalario(e1, int(input("Introduce el salario de tu empleado: ")))

if e1.salario >= 3000:
    print("\nNombre:", e1.nombre, "\nEdad:", e1.edad, "\nSalario:", e1.salario, "\nDebe pagar impuestos.\n")
else:
    print("\nNombre:", e1.nombre, "\nEdad:", e1.edad, "\nSalario:", e1.salario, "\nNo debe pagar impuestos.\n")

print("Ejercicio 6: \n")

listaHijos = []

class Familia():
    def __init__(self, padre:str, madre:str, hijos:list):
        self.padre = padre
        self.madre = madre 
        self.hijos = hijos
    def  __str__(self):
        return f'''
        Familia:
        Madre: {self.madre}
        Padre: {self.padre}
        Hijos: {self.hijos}
        '''

numHijos = int(input("Introduce el número de hijos: "))

for i in range(numHijos):
    hijo = input(f"Introduce el nombre del hijo N° {i+1} : ")
    listaHijos.append(hijo)
f1 = Familia("Marta", "Carlos", listaHijos)

print(f1)


        