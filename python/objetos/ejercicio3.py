#Vamos a
#definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la anterior.
#Cuando se crea esta nueva clase, además del titular y la cantidad se debe
#guardar una bonificación que estará expresada en tanto por ciento.Construye los
#siguientes métodos para la clase:
#En
#esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de
#edad., por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el
#titular es mayor de edad pero menor de 25 años y falso en caso contrario.
#Además
#la retirada de dinero sólo se podrá hacer si el titular es válido.
#El
#método mostrar() debe devolver el mensaje de “Cuenta
#Joven” y la bonificación de la cuenta.

class cuenta:
    def __init__(self):
        self.titular=input("Ingrese nombre del titular: ")
        self.edad=int(input("Ingrese su edad: ")) 
        self.cantidad=float(input("Dinero en cuenta: "))
    def mostrar(self):
        print("Nombre del titular de la cuenta: ",self.titular)
        print("El titular de la cuenta tiene",self.edad,"años")
        print("Saldo en la cuenta: ",self.cantidad) 
    def ingresar(self):
        nuevoingreso=float(input("Monto a ingresar en la cuenta: "))    
        self.cantidad=self.cantidad+nuevoingreso
        print("El nuevo saldo en cuenta es: ",self.cantidad)  
    def retirar(self):   
        nuevoretiro=float(input("Ingrese monto a retirar de la cuenta: "))
        self.cantidad=self.cantidad-nuevoretiro
        if self.cantidad<0:
            print("Tienes saldo negativo", self.cantidad)       
class cuentajoven(cuenta):
    def __init__ (self):
        super().__init__()
        self.Valido=False
    def TitularValido(self):
        if self.edad > 17 and self.edad < 25:
            self.Valido=True
            print("Edad valida para bonificación")
            self.valida=True
            return True
        if self.valida == False:
            return False
    def ingresar(self):
        if self.TitularValido==True:
            print("Tienes un descuento de 20% ")
            self.cantidad=self.cantidad -(self.cantidad*20/100)
    def retirar(self):
        if self.TitularValido==True:
            nuevoretiro=float(input("Ingrese monto a retirar de la cuenta: "))
            self.cantidad=self.cantidad-nuevoretiro
        if self.cantidad<0:
            print("Tienes saldo negativo", self.cantidad)     
    def mostrar(self):
        if self.TitularValido==True:
            print("Se crea cuenta joven")
        elif self.edad<18:
            print("Aún no puedes abrir una cuenta porque eres menor de edad")
        else:
            print("Las cuentas para adultos no tienen bonificacion")


p1=cuentajoven()
p1.ingresar()
p1.retirar()
p1.mostrar()  


