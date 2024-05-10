class coche:
    ruedas=4
    def __init__(self,color,aceleracion):
        self.color=color
        self.aceleracion=aceleracion
        self.velocidad=0
    def acelera(self):
        self.velocidad=self.velocidad+self.aceleracion
    def frena(self):
#        V=velocidad.self-self.aceleracion
        if V<0:
            V=0
        self.velocidad=V
cl=coche("rojo",20)
print(cl.color,cl.aceleracion,cl.ruedas)            

