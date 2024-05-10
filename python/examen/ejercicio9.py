#Cargar un vector de 100 posiciones con numero enteros, a
#partir de este crear 2 vectores; uno con los números pares y el
#otro con los numero impares, además decir de los vectores
#cual es más grande y el número de elementos en cada vector.
#Inicialmente los vectores estarán limpios, esto quiere decir
#que todas las posiciones tendrán el valor 0 (cero). 


Vector = []
print ("Ingrese dimensión del vector: ")
tamaño = int( input())
pares = tamaño*[0]
impares = tamaño*[0]
print ( "Ingrese los", tamaño, "valores del vector")
for x in range(tamaño):
    ingreso = int( input("Elemento {}: ".format(x+1)))
    Vector.append(ingreso)
    par = 0
    impar = 0
for x in range(tamaño):
    if Vector[x] % 2 == 0:
        pares[par] = Vector[x]
        par = par + 1
    else:
        impares[impar] = Vector[x]
        impar = impar + 1
print("Elementos del vector par",pares[0:par]) 
print ( "El vector de pares tiene" , par, "elementos")
print("Elementos del vector impar",impares[0:impar])
print ( "El vector de impares tiene", impar, "elementos")
if par > impar :
    print ( "El vector de pares es el más grande")
elif par < impar:
    print ( "El vector de impares es el mas grande")
else:
    print ( "Los 2 vectores son iguales en número de elementos")