def bisiesto(anio):
    if anio % 4 == 0:
        resultado=1
        if anio % 100==0:
            resultado=0
            if anio % 400==0:
                resultado=1 
    else:
        resultado=0
    return resultado

juliano=0
durmes=[0,31,28,31,30,31,30,31,31,30,31,30,31]
#dia=int(input("Ingrese el dia: "))
#mes=int(input("Ingrese el mes: "))
#anno=int(input("ingrese el año: "))
lista=[]
fecha=input("ingrese la fecha separada por : / / ")
lista=fecha.split("/")
dia=int(lista[0])
mes=int(lista[1])
anno=int(lista[2])
if mes==1:
    juliano=dia
else:

    for i in range(1,mes):
        juliano+=durmes[i]
    if juliano>58 and bisiesto(anno)==1:
        juliano+=1
    juliano+=dia
print("El numero de dia juliano es", juliano)