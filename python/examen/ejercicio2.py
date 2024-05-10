#Dado el tiempo en segundos y la distancia en metros de un móvil, ingresados por
#teclado, calcule la velocidad correspondiente. 

tiempo=int(input("Ingrese el tiempo en segundos: "))
distancia=int(input("Ingrese la distancia en metros: "))

velocidad= distancia/tiempo

print("El automovil recorrera: ", velocidad, "metros por segundos")