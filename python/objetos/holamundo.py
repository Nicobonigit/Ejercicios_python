from tkinter import *
from random import randint
import random
from tkinter.messagebox import *

letrasUsadas=[]
vidas= 7


def vidas_s():
    print(vidas.get())


def probarLetraFuncion():
    global vidas
    letrasUsadas.append(letraObtenida.get())
    print(letrasUsadas)
    if letraObtenida.get() in palabra:
        if palabra.count(letraObtenida.get())>0:
            for i in range(len(palabra)):
                if palabra[i]==letraObtenida.get():
                    guiones[i].config(text=""+letraObtenida.get())
            else:
                guiones[palabra.index(letraObtenida.get())].config(text=""+letraObtenida.get())
    else:
        vidas-=1
        if vidas==0:
            showwarning(title="Derrota",message="Se te acabaron las vidas")

raiz = Tk()

archivo = open("termino.txt","r")
conjuntoPalabras= list(archivo.read().split("\n"))
palabra = conjuntoPalabras[random.randint(0,len(conjuntoPalabras)-1)].lower()
letraObtenida=StringVar()


raiz.config(width=1000, height = 600, bg="blue",relief = "groove",bd=10)
juegoFrame = Frame(raiz)
juegoFrame.config (width=1000, height = 600,relief = "sunken",bd=15)
juegoFrame.grid_propagate(False)

juegoFrame.pack()

Label(juegoFrame,text= "Introduce una letra", font=("Verdana", 24), #Cartel en Pantalla.
    ).grid(row=0, column=0,padx=10,pady=10)
letra= Entry(juegoFrame,width=1,font=("Verdana", 24),textvariable=letraObtenida
             ). grid(row=0, column=1,padx=10,pady=10)
probarLetra = Button(juegoFrame,text="Probar",bg="yellow",command=probarLetraFuncion
                     ).grid(row=1,column=0,pady=10)

guiones = [Label(juegoFrame,text="_",font=("verdana",30)) for  _ in palabra ]

inicialX=200
for i in range(len(palabra)):
    guiones[i].place(x=inicialX,y=400)
    inicialX+=50
  
Label(juegoFrame,text= " 7 vidas.", font=("Verdana", 24),textvariable=vidas_s #DUDA ACA
    ).grid(row=0, column=80,padx=10,pady=10)    

vidas_s = StringVar()

raiz.mainloop()