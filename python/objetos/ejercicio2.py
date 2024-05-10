#Crea una
#clase llamada Cuenta que tendrá los siguientes
#atributos: titular (que es una persona) y cantidad (puede tener decimales). El
#titular será obligatorio y la cantidad es opcional. Construye los siguientes
#métodos para la clase:
#mostrar(): Muestra los datos de la cuenta.
#ingresar(cantidad): se ingresa una cantidad a la cuenta, si
#la cantidad introducida es negativa, no se hará nada.
#retirar(cantidad): se retira una cantidad a la cuenta. La
#cuenta puede estar en números rojos.


class cuenta:
    def __init__(self):
        self.titular=input("Ingrese nombre del titular: ")
        self.cantidad=float(input("Dinero en cuenta: "))
    def mostrar(self):
        print("Nombre del titular de la cuenta: ",self.titular)
        print("Saldo en la cuenta: ",self.cantidad)
        return
    def ingresar(self):
        nuevoingreso=float(input("Monto a ingresar en la cuenta: "))    
        self.cantidad=self.cantidad+nuevoingreso  
        print("El saldo en cuenta es: ",self.cantidad)
    def retirar(self):   
        nuevoretiro=float(input("Ingrese monto a retirar de la cuenta: "))
        self.cantidad=self.cantidad-nuevoretiro
        print("Nuevo saldo en cuenta: ",self.cantidad)
        if self.cantidad<0:
            print("Tienes saldo negativo",self.cantidad)
        else:
            print("Este es tu nuevo saldo en cuenta: ",self.cantidad)         
        return
p1=cuenta()
p1.mostrar()    
p1.ingresar()
p1.retirar()
