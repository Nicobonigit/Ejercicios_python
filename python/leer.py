
Archivo = open("termino.txt")
linea=Archivo.readline()
pala=len(linea)
listado=[]
x=0
for i in range(pala):  
    listado.append(linea.rstrip())     
    linea=Archivo.readline()    
    x+=1 
print (listado)
print("Caracteres en la linea",pala)
Archivo.close()
