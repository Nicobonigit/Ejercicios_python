Archivo=open("deprueba.txt","r")
lista=Archivo.readlines()
listas=[]
pala=len(lista)
for lineas in lista:    
    listas.append(lineas.strip())
print("Lineas de este archivo:",pala)
print (listas)
Archivo.close()
