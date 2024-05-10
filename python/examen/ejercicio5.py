#Para una empresa con N empleados, se desarrolla un algoritmo donde se ingresa como 
#datos el número de orden y sueldo de cada empleado, debe imprimirse el numero de 
#orden del empleado con el mayor sueldo asi como su sueldo. Haga el algoritmo 
#correspondiente.

i = 1
empleadom = 0
mayorsueldo = 0
cant_e = int( input("Ingrese la cantidad de empleados:"))

print("Ingrese los sueldos de a uno.")
for i in range(cant_e):
    sueldo = int( input("Sueldo del empleado N°{0}: ".format(i+1)))  
    if sueldo > mayorsueldo:
        mayorsueldo = sueldo
        empleadom=i+1


print ("El empleado de mayor sueldo es el N°: ",empleadom, "y percibe un sueldo de:",mayorsueldo)

