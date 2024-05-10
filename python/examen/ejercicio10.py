#Desarrollar un programa en Python que permita cargar por teclado un texto. Siempre se supone que usuario cargará
#un punto para indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco.
#El programa debe determinar:
#a) La cantidad de palabras que comienzan con la expresión "pa" y termina con la letra "n"
#b) La cantidad de palabras que presentan mas de dos vocales a partir de la tercera letra de la palabra
#c) El porcentaje que representa la cantidad de palabras del punto anterior respecto de la cantidad de total de
#palabras del texto
#d) Cantidad de palabras de mas de 5 letras

texto=input("Escriba un texto: ")
listatexto=texto.split(".")
vocal=("a","e","i","o","u")
contpa=0
palabra5=0
V=0
contvocal=0
largolistatexto=len(listatexto)
for i in range(largolistatexto):
    separador=listatexto[i].split(" ")
    for j in range(len(separador)):
        palabra=separador[j]
        f=len(palabra)
        f=f-1
        if palabra[0:2]=="pa" and palabra[f]=="n":
            contpa+=1
        if f>4:
            palabra5+=1
        if f>=3:            
            for l in range(3,f,1):
                    if palabra[l] in vocal:
                        V+=1
                        if V==2:
                           contvocal+=1                          
                    else:
                        ("FIN")
print("Resultado punto A): ",contpa)
print("Resultado punto B): ",contvocal)
print("Resultado punto D): ",palabra5)


