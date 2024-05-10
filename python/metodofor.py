Archivo=open("deprueba.txt","r")
lista=Archivo.readlines()
listas=[]
pala=len(lista)

for i in range (pala):    
    listas.append(lista[i].strip())
print (pala)
print (listas)
Archivo.close()