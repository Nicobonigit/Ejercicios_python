import random

numeros = ['1','2','3','4','5','6','7','8','9','10','11','12']
palos = ['oro','Espadas','copas','basto']
baraja = []

for n in numeros:
    for p in palos:
        union = f"{n} de {p}"
        baraja.append(union)  
#print(baraja)#arma el maso uniendo los numeros a los palos            
random.shuffle(baraja)
#print("--------------------------------------mezcla y arma el mazo-----------------------------------------------")

#print(baraja) 

#print("--------------------------------------reparte-------------------------------------------------------------")

for i in range (0,48,2):
    for j in range(2):
        print("{:14}".format(baraja[i+j]), end = " ")
    print()

#print()    
#print("--------------------------------------reparte-------------------------------------------------------------")

jugador1=[]
jugador2=[]
cont1=0
cont2=0

print("--------------------------------------inicia el juego-------------------------------------------------------------")

for i in range (24):
        carta1=baraja.pop(0)
        jugador1.append(carta1)
        carta2=baraja.pop(0)
        jugador2.append(carta2)
        print(carta1,"/vs/",carta2)
        f=int (carta1[0:2])
        g=int (carta2[0:2])
        if f>g:
            cont1+=1
        elif f<g:
            cont2+=1
        
print(cont1,cont2)
if cont1>cont2:
    print("Gana jugador1")
elif cont1<cont2:
    print("Gana jugador2")  
else: print("Empate")