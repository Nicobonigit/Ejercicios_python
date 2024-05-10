# Pedir al usuario que ingrese el sueldo y la antigüedad del operario
sueldo = float(input("Ingrese el sueldo del operario: "))
antiguedad = int(input("Ingrese los años de antigüedad del operario: "))

# Verificar las condiciones y aplicar los aumentos correspondientes
if sueldo < 500 and antiguedad >= 10:
    # Aumento del 20% si el sueldo es inferior a 500 y la antigüedad es igual o superior a 10 años
    aumento = sueldo * 0.2
    sueldo_nuevo = sueldo + aumento
    print("Se aplicó un aumento del 20%. Sueldo a pagar: ", sueldo_nuevo)
elif sueldo < 500 and antiguedad < 10:
    # Aumento del 5% si el sueldo es inferior a 500 pero la antigüedad es menor a 10 años
    aumento = sueldo * 0.05
    sueldo_nuevo = sueldo + aumento
    print("Se aplicó un aumento del 5%. Sueldo a pagar: ",sueldo_nuevo)
else:
    # Si el sueldo es mayor o igual a 500, no hay cambios
    print("Sueldo sin cambios:", sueldo)
