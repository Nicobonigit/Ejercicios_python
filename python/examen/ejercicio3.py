#Dado el sueldo de un trabajador, aplique un aumento del 15% si su sueldo es inferior a
#$1000. Imprima el sueldo que percibirá.

sueldo = int(input("Ingrese su sueldo: "))
if sueldo < 1000:
    sueldo = sueldo + (sueldo * 0.15)    
print("El trabajador percibirá: ", sueldo, "de sueldo.")