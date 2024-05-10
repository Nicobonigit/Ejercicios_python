Archivo = open("termino.txt")
linea=Archivo.readline()
listado=[]
i=0
while linea !=(""):
    i+=1
    listado.append(linea.rstrip())    
    linea=Archivo.readline()
print(listado)
print("Lineas en el archivo",i)
Archivo.close()
