print("-------------------------------------------------------")
print("Matriz3: SUCURSALES DE UNA EMPRESA.")
print("-------------------------------------------------------")
#Inicializar
MONTO = [] #Se crea una lista vacía
#Entradas
print("Ingrese número de sucursales y años: ")
N = int( input("Número de Sucursales: "))
M = int( input("Número de Años: "))
for i in range(M):
    MONTO.append([]) 
    for j in range(N):
        print("Ingrese ventas de la sucursal", j+1 , "en el año", i+1 )
        venta = int( input())       
        MONTO[i].append(venta)    

#Proceso
print("\nSUCURSAL CON MÁS VENTAS: ")
print("-------------------------------------------------------")
MAX = 0
for j in range(N):
    SUMA = 0
    for i in range(M):
        SUMA = SUMA + MONTO[i][j]
print ("Número de ventas de la Sucursal" , j+1, "es", SUMA)
if SUMA > MAX :
    MAX = SUMA
SUC = j + 1 #Se incrementa j, por conteo desde 0
print("Sucursal que más vendió: ", SUC)
print("\nPROMEDIO DE VENTAS DEL AÑO: ")
print("-------------------------------------------------------")
MAX = 0
for i in range(M):
    SUMA = 0
for j in range(N):
    SUMA = SUMA + MONTO[i][j]
PROM = SUMA/N
print ("Promedio de ventas del año" , i+1, "es", PROM)
if PROM > MAX :
    MAX = PROM
ANIO = i + 1 #Se incrementa i, por conteo desde 0
print("Año con mayor promedio", ANIO)