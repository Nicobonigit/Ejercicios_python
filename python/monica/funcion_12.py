def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

# Ejemplo de uso
numero1 = 50
numero2 = 25
resultado = calcular_mcd(numero1, numero2)
print(f"El MCD de {numero1} y {numero2} es {resultado}.")
