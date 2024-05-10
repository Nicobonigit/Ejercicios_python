def calcular_mcd_tres_numeros(a, b, c):
    # Función para calcular el MCD de dos números
    def calcular_mcd_dos_numeros(x, y):
        while y:
            x, y = y, x % y
        return abs(x)

    # Calcula el MCD de los dos primeros números
    mcd_ab = calcular_mcd_dos_numeros(a, b)

    # Calcula el MCD final con el tercer número
    mcd_final = calcular_mcd_dos_numeros(mcd_ab, c)

    return mcd_final

# Ejemplo de uso
numero1 = 24
numero2 = 36
numero3 = 48
resultado = calcular_mcd_tres_numeros(numero1, numero2, numero3)
print(f"El MCD de {numero1}, {numero2} y {numero3} es {resultado}.")
