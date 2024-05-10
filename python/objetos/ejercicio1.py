#Vamos a
#crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
#Construye los siguientes métodos para la clase:
#mostrar(): Muestra los datos de la persona.
#esMayorDeEdad(): Devuelve un valor lógico indicando si
#es mayor de edad.

class Persona:
    def __init__(self):
        self.nombre=input("Ingrese su nombre: ")
        self.edad=int(input("Ingrese su edad: "))
        self.dni=int(input("Ingrese su dni: "))
    def mostrar(self):
        print(self.nombre)
        print(self.edad)
        print(self.dni)
    def esmayor(self):
        if self.edad>18:
            print(self.nombre,"es mayor de edad")
        else:
            print("Es menor")
        
p1=Persona()
print(p1.nombre,p1.edad,p1.dni)
print(p1.esmayor())