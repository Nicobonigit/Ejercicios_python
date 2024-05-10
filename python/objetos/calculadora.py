class calculadora:
    def __init__(self):
        self.n1=int(input("Ingresa un numero: "))
        self.n2=int(input("Ingresa un numero: "))
    def suma(self):
        self.sum=self.n1+self.n2
        print("La suma de los numeros es: ",self.sum)
    def resta(self):
        self.rest=self.n1-self.n2
        print("La resta de los numeros es: ",self.rest)
    def multiplicacion(self):
        self.multiplicacio=self.n1*self.n2
        print("La multiplicación de los números es: ",self.multiplicacio)
    def division(self):
        if  self.n2 == 0:
            print("No se puede dividir sobre cero")
        else:
            self.divisio=self.n1/self.n2
            print("La division de los numeros es: ",self.divisio)
        

op=calculadora()
op.suma()
op.resta()
op.multiplicacion()
op.division()