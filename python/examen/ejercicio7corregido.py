#Una empresa automotriz necesita un programa para manejar los montos de ventas de 
#sus N sucursales, a lo largo de los últimos M años. Los datos son dados de esta forma: 
#M, N 
#MONTO 1 1 MONTO 1 2 ..... MONTO 1 N 
#MONTO 2 1 MONTO 2 2 ..... MONTO 2 N 
#MONTO M 1 MONTO M 2 ..... MONTO M N 
#Donde: 
#M es una variable entera que representa el número de años entre 1 y 30 inclusive. 
#N es una variable entera que representa el número de sucursales de la empresa entre 
#1 y 35 inclusive. 
#MONTO i j Variable real (matriz de 2 dimensiones) representa lo que se vendió en el 
#año I en la sucursal J 
#La información que necesitan los directores de la empresa para tomar decisiones es la 
#siguiente: 
#a.Sucursal que más ha vendido en los M años. 
#b.Promedio de ventas por año. 
#c.Año con mayor promedio de ventas



i=0
j=0
print("Ingrese número de sucursales y años: ")
S = int( input("Número de Sucursales: "))
A = int( input("Número de Años: "))

#Define the matrix
montos = [ ]

for i in range(A):          # A for loop for row entries
    a =[ ]
    for j in range(S):      # A for loop for column entries
        print("Ingrese ventas de la sucursal", j+1 , "en el año", i+1 )
        a.append(int(input()))
    montos.append(a)

#To print the matrix
for i in range(A):
    for j in range(S):
        print(montos[i][j], end = " ")
    print( )

MAX=0
SUCMAX=0
TOTALVENTAS=0
for i in range(S):
    SUM=0
    for j in range(A):
        SUM=SUM+montos[j][i] 
        TOTALVENTAS=TOTALVENTAS+montos[j][i]
    if MAX < SUM:
        MAX=SUM
        SUCMAX=i+1

PROMVENTAS = TOTALVENTAS/A

print("La sucursal de mayores ventas es la " + str(SUCMAX) + " con un monto total de " + str(MAX))
print("El promedio de venta por anio es " + str(PROMVENTAS))

PROMANIO=0
MAXAN=0
for j in range(A):
    SUMANIO=0
    for i in range(S):
        SUMANIO=SUMANIO+montos[j][i]
    if PROMANIO < SUMANIO:
        PROMANIO=SUMANIO
        MAXAN=j+1

print("El anio con mayor promedio es " + str(MAXAN) + " con un promedio de " + str(PROMANIO/S))