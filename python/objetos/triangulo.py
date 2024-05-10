class triangulo:
    def __init__(self):
        self.ladoA=int(input("Ingrese el tamaño del lado:"))
        self.ladoB=int(input("Ingrese el tamaño del lado:"))
        self.ladoC=int(input("Ingrese el tamaño del lado:"))
    def mostrar(self):
        print("El lado A es:",self.ladoA)
        print("El lado B es:",self.ladoB)
        print("El lado C es:",self.ladoC)
    def mayor(self):
        if self.ladoA > self.ladoB and self.ladoA > self.ladoC:
            print("El lado A es el mayor")
        if self.ladoA == self.ladoB and self.ladoB == self.ladoC:
            print("Todos los lados son iguales")      
        elif self.ladoB > self.ladoA and self.ladoB > self.ladoC:
            print("El lado B es el mayor")  
        else:
            print("El lado C es el mayor")
    def tipo(self):
        if self.ladoA == self.ladoB and self.ladoA == self.ladoC:
            print("El triangulo es equilatero")
        elif self.ladoA != self.ladoB and self.ladoB != self.ladoC and self.ladoA != self.ladoC:
            print("El triangulo es escaleno")
        else:
            print("El triangulo es isosceles")

tri=triangulo()
tri.mostrar()
tri.mayor()
tri.tipo()