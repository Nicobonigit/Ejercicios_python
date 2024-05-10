class persona:
    def __init__(self):
        self.nombre=input("Ingrese su nombre: ")
        self.edad=int(input("Ingrese su edad: "))
    def mostrar(self):
        print(self.nombre)
        print(self.edad)
class empleado:
    def __init__ (self):
        super().__init__()
        self.sueldo=int(input("Ingrese sueldo: "))
    def pagaimpuesto(self):
        if self.sueldo > 3000:
            print("Paga impuesto")
        else:
            print("No paga impuesto")


p=persona()
e=empleado()
e.pagaimpuesto()
print(p.mostrar())