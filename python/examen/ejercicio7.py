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

montos = [] 
print("Ingrese número de sucursales y años: ")
S = int( input("Número de Sucursales: "))
A = int( input("Número de Años: "))

for i in range(A):
    montos.append([]) 
    
    for j in range(S):
        print("Ingrese ventas de la sucursal", j+1 , "en el año", i+1 )
        venta = int( input())       
        montos[i].append(venta)
MAX = 0
for j in range(S): 
    SUMA = 0
    for i in range(A):
        SUMA = SUMA + montos[i][j]
    print ("Número de ventas de la Sucursal" , j+1, "es", SUMA)
if SUMA > MAX :
    MAX = SUMA
    SUC = j +1 
    print("Sucursal que más vendió: ", SUC)
ventasanuales=0
for j in range(A):
    SUMA=0
    PROM=0
    for x in range(S):
        ventasanuales=0
        annomayorventas=0
        SUMA = SUMA + montos[j][x]            
    ventasanuales=SUMA/S
    print("Promedio en ventas correspondientes al año:",j+1,": ", ventasanuales)

    

