#Construir un programa que, dado como datos el radio y la altura de un cilindro, calcule
# e imprima el área y su volumen

from math import pi

radio = int(input("Indique el radio: "))
altura= int(input("Indique la altura: "))

area = 2 * pi * radio**2 + 2 * pi * radio * altura
volumen = pi * radio**2 * altura

print("El area del cilindro es: ", area)
print("El volumen de cilindro es: ",volumen)