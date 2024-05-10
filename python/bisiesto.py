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
print(bisiesto(2004))