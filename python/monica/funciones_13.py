# Definir listas con los nombres de los planetas y sus distancias al Sol
planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]
distancias_al_sol = [57.91, 108.2, 149.6, 227.9, 778.3, 1427.0, 2871.0, 4497.1]

# Mostrar el listado numerado de los planetas
print("Listado de planetas:")
for i, planeta in enumerate(planetas, 1):
    print(f"{i}. {planeta}")

# Pedir al usuario que ingrese el número del planeta que desea consultar
while True:
    try:
        numero_planeta = int(input("Ingrese el número del planeta que desea consultar: "))
        if 1 <= numero_planeta <= len(planetas):
            break
        else:
            print("Número de planeta fuera de rango. Inténtelo de nuevo.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Obtener el nombre y la distancia del planeta seleccionado
planeta_seleccionado = planetas[numero_planeta - 1]
distancia_media = distancias_al_sol[numero_planeta - 1]

# Mostrar la distancia media al Sol del planeta seleccionado
print(f"La distancia media de {planeta_seleccionado} al Sol es: {distancia_media} millones de kilómetros.")
