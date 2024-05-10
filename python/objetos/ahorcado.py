from tkinter import *
import random

App = Tk()
App.geometry('1280x720')
App.resizable(width=0, height=0)
App.title("Ahorcado")
App.config(bg="green4")
vidas = 6

#Fondo-----------------------------------------------------------------------------------------------------

Canvas = Canvas(App, width=1280, height=720)
Canvas.pack()

Fondo = PhotoImage(file="fondo.png")
imagen_id = Canvas.create_image(640, 360, image=Fondo)

Titulo= PhotoImage(file="Titulo.png")
imagen_id1 = Canvas.create_image(640, 400, image=Titulo)

Horc= PhotoImage(file="Horca 01.png")
imagen_id10 = Canvas.create_image(640, 360, image=Horc)

#-----------------------------------------------------------------------------------------------------------
#Imagenes-----------------------------------------------------------------------------------------------------

Horca1 = PhotoImage(file="Horca 01.png")
Horca2 = PhotoImage(file="Horca 02.png")
Horca3 = PhotoImage(file="Horca 03.png")
Horca4 = PhotoImage(file="Horca 04.png")
Horca5 = PhotoImage(file="Horca 05.png")
Horca7 = PhotoImage(file="Horca 06.png")
Horca8 = PhotoImage(file="Horca 07.png")


#-----------------------------------------------------------------------------------------------------------
Palabras=["PELO"]
Palabra=random.choice(Palabras)
N=len(Palabra)
Letras_usadas = []
Letras_acertadas=0

Vector=str(Palabra)
Vector2=[Label(Canvas, text="_", font=("Cheveuxdange",32), background="#087230", fg="#ffffff") for _ in Palabra]
InicialX=100
for i in range(N):
    Vector2[i].place(x=InicialX, y=300)
    InicialX+=50

A=0
x=0
c=0

label_vidas = Label(Canvas, text="Vidas: " + str(vidas), font=("Cheveuxdange", 24), background="#087230", fg="#ffffff")
label_vidas.place(x=1000, y=100)

label = Label(Canvas, text="Introduce una letra", font=("Cheveuxdange",32), background="#087230", fg="#ffffff")
label.place(x=80, y=170)
Letra = Entry(Canvas, width=2, font=("Bebas Neue",26))
Letra.place(x=480, y=180)
Letra.config(justify=CENTER)

def procesar_letra(event=None):
    global Letras_acertadas
    global vidas
    letra = Letra.get()  # valor caja de texto
    Letra.delete(0, END)  # eliminar contenido
    Letra1=letra.upper()
    print("La letra ingresada es:", Letra1)  # mostrar letra

    if Letra1 in Letras_usadas:
        vidas-=1
        label_vidas.config(text="Vidas: " + str(vidas)) # actualizar label
        label.config(text="Letra repetida", fg="red")
        if vidas == 0:
            label.config(text="GAME OVER, la palabra era: " + Palabra, fg="red")
    elif Letra1 in Vector:
        for i in range(N):
            if Letra1 == Vector[i]:
                    Vector2[i].config(text=Letra1)
                    Letras_acertadas+=1
        label.config(text="Acertaste una letra", fg="#ffffff")
        print(Letras_acertadas)
    else:
        vidas -= 1
        label_vidas.config(text="Vidas: " + str(vidas))
        label.config(text="Letra equivocada", fg="red")

    if vidas == 0:
        label.config(text="GAME OVER, la palabra era: " + Palabra, fg="red")
        Letra.config(state=DISABLED)
    if vidas == 5:
        imagen_id2 = Canvas.create_image(640, 360, image=Horca2)
    elif vidas == 4:
        imagen_id2 = Canvas.create_image(640, 360, image=Horca3)
    elif vidas == 3:
        imagen_id2 = Canvas.create_image(640, 360, image=Horca4)
    elif vidas == 2:
        imagen_id2 = Canvas.create_image(640, 360, image=Horca5)
    elif vidas == 1:
        imagen_id2 = Canvas.create_image(640, 360, image=Horca7)
    elif vidas == 0:
        imagen_id2 = Canvas.create_image(640, 360, image=Horca8)

    if Letras_acertadas==N:
        label.config(text="Ganaste", fg="#ffffff")
        Letra.config(state="disabled")
    Letras_usadas.append(Letra1)


Letra.bind("<Return>", procesar_letra)

if Letras_acertadas==N:
        Letra.config(DISABLED)

App.mainloop()