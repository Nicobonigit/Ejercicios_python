class animal:
    def __init__(self,color,peso,alimentacion,comio=True,defeco=False):
        self.color=color
        self.peso=peso
        self.alimentacion=alimentacion
perro=animal("negro",50,"carne")
print(perro.color,perro.peso,perro.alimentacion)
    