def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

while True:
    # Mostrar el menú
    print("Menú:")
    print("1. Sumar dos números.")
    print("2. Restar dos números.")
    print("3. Multiplicar dos números.")
    print("4. Dividir dos números.")
    print("5. Salir.")

    # Pedir al usuario que ingrese una opción
    opcion = input("Seleccione una opción (1-5): ")

    # Verificar que la opción sea válida
    if opcion.isdigit() and 1 <= int(opcion) <= 5:
        opcion = int(opcion)
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")
        continue

    # Salir del bucle si la opción es 5
    if opcion == 5:
        print("¡Hasta luego!")
        break

    # Pedir al usuario que ingrese dos números
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    # Ejecutar la opción seleccionada del menú
    if opcion == 1:
        resultado = sumar(numero1, numero2)
    elif opcion == 2:
        resultado = restar(numero1, numero2)
    elif opcion == 3:
        resultado = multiplicar(numero1, numero2)
    elif opcion == 4:
        resultado = dividir(numero1, numero2)

    # Mostrar el resultado
    print(f"El resultado es: {resultado}")
    print()
