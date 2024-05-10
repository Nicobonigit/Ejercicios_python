#Desarrollar un programa para implementar un juego de cartas de la baraja española. Es una competencia de n rondas
#entre 2 jugadores (n se carga por teclado, validar) En cada ronda, cada jugador recibe una carta 
#(cuyo número y palo el programa deberá generar de forma aleatoria) y se define la ronda de la siguiente manera:
#El jugador que tenga la carta de mayor valor, se lleva ambas.Si las cartas son del mismo valor, 
#se las lleva quien tenga una carta de oro. Si ambos tienen oro o ninguno lo tiene, cada jugador recupera su carta.
#Los puntos de cada jugador se determinan sumando los valores de todas las cartas que 
#ganó. Será triunfador el que tenga mayor puntaje total.
import random

cartas = ['1','2','3','4','5','6','7','8','9','10','11','12']
palos = ['oro','Espadas','copas','basto']
baraja = []

for p in palos:
    for c in cartas:
        union = f'{c} de {p}'
        baraja.append(union)        

jugador1=int(input("Si desea detener el juego presione 0 y vea el resultado final:"))
jugador2=int(input("Si desea detener el juego presione 0 y vea el resultado final:"))

contjug1=0
contjug2=0

for i in range (1,4):
    while jugador1 !=0:
        jugada1=random.choice(baraja)        
        print(jugada1)
#        for x in range(len(baraja)):
#            if baraja[jugada1]==jugada1:
#                print(baraja.pop(x))         
        break
    while jugador2 !=0:
        jugada2=random.choice(baraja)
#        for j in range(len(baraja)):
#            if baraja[jugador2]==jugada2:
#                print(baraja.pop(j))
        print(jugada2)
        break
    jugador1=int(input("Si desea detener el juego presione 0 y vea el resultado final:"))
    jugador2=int(input("Si desea detener el juego presione 0 y vea el resultado final:"))
    if jugada1 > jugada2:
        contjug1+=2
    elif jugada1==jugada2:
        contjug1=contjug1
        contjug2=contjug2
    else:
        contjug2+=2
print(contjug1)
print(contjug2)
if contjug1>contjug2:print("Ganó el jugador 1")
else:print("ganó jugador 2")