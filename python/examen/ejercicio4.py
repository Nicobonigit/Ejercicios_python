#Algoritmo, que dada una fecha (representada por el día, el mes y el año en formato 
#numérico dd/mm/aaaa), calcule el día siguiente.



def siguientefecha (diaa, mess, anio):
    if anio % 4 == 0:
        bisiesto=True
        if anio % 100==0:
            bisiesto=False
            if anio % 400==0:
                bisiesto=True
    else:
        bisiesto=False
       

    if mess in (1,3,5,7,8,10,12):
        diames = 31
    elif mess == 2:
        if bisiesto:
            diames = 29
        else:   
            diames = 28
    else:
        diames = 30

    if diaa<diames:
        diaa+=1
    else:
        diaa=1
        if mess==12:
            mess=1
            anio+=1
        else:
            mess+=1
    return (diaa,mess,anio)



diaa1=0
mess1=0
anio1=0
fecha=input("ingrese la fecha separada por : / / \n")
fecha1=fecha.split("/")
diaa1=fecha1[0]
diaa1=int(diaa1)
mess1=fecha1[1]
mess1=int(mess1)
anio1=fecha1[2]
anio1=int(anio1)
var=siguientefecha(diaa1,mess1,anio1)
df=var[0]
mf=var[1]
af=var[2]
if diaa1 >= 32 or mess1 >= 13:
    print("Ingresaste una fecha INVALIDA, ingresa una valida para continuar")
    fecha=input("ingrese la fecha separada por : / / \n")
    diaa1=0
    mess1=0
    anio1=0    
    fecha1=fecha.split("/")
    diaa1=fecha1[0]
    diaa1=int(diaa1)
    mess1=fecha1[1]
    mess1=int(mess1)
    anio1=fecha1[2]
    anio1=int(anio1)
    var=siguientefecha(diaa1,mess1,anio1)
    df=var[0]
    mf=var[1]
    af=var[2]
    
print("Mañana será",df,"/",mf,"/",af)



    
