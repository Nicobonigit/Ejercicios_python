###Crear una funcion a la que se le pasa un numero entero y devuelve la cantidad de
###divisores primos que tiene.

def contar_divisores_primos(numero):
    # Función para verificar si un número es primo
    def es_primo(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Contador de divisores primos
    contador = 0

    # Iterar sobre los números desde 1 hasta el número dado
    for i in range(1, numero + 1):
        # Verificar si i es divisor de numero y primo
        if numero % i == 0 and es_primo(i):
            contador += 1

    return contador
numero = 12
resultado = contar_divisores_primos(numero)
print(f"El número {numero} tiene {resultado} divisores primos.")
