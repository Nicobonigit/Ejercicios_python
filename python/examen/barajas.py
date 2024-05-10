import random
cartas = ['1','2','3','4','5','6','7','8','9','10','11','12']
palos = ['oro','Espadas','copas','basto']
baraja = []

for p in palos:
    for c in cartas:
        union = f'{c} de {p}'
        baraja.append(union)      
random.shuffle(baraja)
print("\n************************* REPARTE ************************************")
variable = 48

for i in range(5):
    print("Jugador {}".format(i+1))
    for j in range(4):
        variable -= 1; a = random.randint(0,variable)
        print("{:15}".format(baraja[a]) ,end=" ")
        baraja.pop(a)
    print()
    
print("\n************************* BARAJA COMPLETA ****************************")

for i in range(len(baraja)):
    if i%4 == 0:
        print()
    print(" {:15} ".format(baraja[i]) , end=" | ")


