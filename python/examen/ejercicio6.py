#Escriba un diagrama de flujo que dado un vector (máximo 200 elementos) ordenado 
#de enteros y con posibles repeticiones de valores, obtenga como salida una lista de los
#números ordenados, pero sin repeticiones.

vector = []
for i in range(1,11):
    valor=int(input("Ingrese un valor: "))
    vector.append(valor) 
sinrepe = vector.copy()
sinrepe=set(vector)
lista=list(set(vector))
lista.sort()
print("El resultado final es:",lista)
