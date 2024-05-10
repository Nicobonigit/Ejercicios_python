contador3=0
contador5=0
contador7=0
contvocales3=0
paconvoca=0
x=0
vocales=("a","e","i","o","u")
texto=input("Ingrese la cadena de caracteres : ")
a=texto.split(" ")
q=0
largotexto=len(a)
largotexto=largotexto-1
for i in range(largotexto):
    a=list(a)
    for q in range(len(a)):
        x=a[q]
        v=a[q]
        x=len(x)
        if x==3:
            contador3+=1
        elif x==5:
            contador5+=1
        elif x==7:
            contador7+=1

        if x>2 and v[2] in vocales:
                contvocales3+=1
        for j in range(len(v)):
            if v[j] in vocales:            
                paconvoca+=1
cantidad=paconvoca*100/largotexto       
print("palabras tienen 3, 5 o 7 letras", contador3)
print("palabras con más de tres letras, que tienen una vocal en la tercera letra",contador5)
print("porcentaje de palabras que tienen sólo una o dos vocales sobre el total de palabras del texto", contador7)