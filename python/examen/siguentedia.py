def bisiesto(anio):
    if anio % 4 == 0:
        resultado=True
        if anio % 100==0:
            resultado=False
            if anio % 400==0:
                resultado=True 
    else:
        resultado=False
    return resultado

dia = 0
mes = 0
anio = 0

sig_dia = 0
sig_mes = 0
sig_anio = 0

mes31 = (1,3,5,7,8,10) 
mes30 = (4,6,9,11) 

while True:    
    print("Ingresa una fecha: ")
    print("Dia: ", end = " ")
    dia = int(input())
    print("Mes: ", end = " ")
    mes = int(input())
    print("Año: ", end = " ")
    anio = int(input())

    sig_dia = dia + 1
    sig_mes = mes

    if mes == 12 and dia == 31:
        sig_dia = 1
        sig_mes = 1
        sig_anio = anio + 1
    else:
        sig_anio = anio

    for i in range(len(mes31)):
        if dia == 31 and mes == mes31[i]:
            sig_dia = 1
            sig_mes = mes + 1
    for i in range(len(mes30))            :
        if dia == 30 and mes == mes30[i]:
            sig_dia = 1
            sig_mes = mes + 1  
    
    
    if mes == 2 and dia == 28:    
        sig_dia = 1
        sig_mes = mes + 1    
    if dia == 29 and mes == 2 and bisiesto == 0:
        sig_dia = 1
        sig_mes = mes + 1

    if dia >= 32 or mes >= 13:
        print("Ingresaste una fecha INVALIDA, favor de escribir fechas reales")
    else:
        print("Dia Ingresado: ", dia, "/", mes, "/", anio) 
        print("Siguiente dia: ", sig_dia, "/", sig_mes, "/", sig_anio)