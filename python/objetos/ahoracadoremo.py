from tkinter import *

class Interfaz:
    def __init__(self, ventana):
        self.puntaje=10
        self.mensaje="PERDISTE"
        self.puntaje1=0
        self.mensaje1="GANASTE"
        self.ventana=ventana
        self.ventana.title("Ahorcado")
        self.operacion=""
        self.pantalla0=Text(ventana, state="disabled", width=10, height=4, background="red", foreground="white", font=("Helvetica",18))
        self.pantalla0.grid(row=0,column=0,columnspan=5)
        self.pantalla1=Text(ventana, state="disabled", width=5, height=4, background="black", foreground="white", font=("Helvetica",18))
        self.pantalla1.grid(row=0,column=3,columnspan=1)
        self.pantalla2=Text(ventana, state="disabled", width=5, height=4, background="black", foreground="white", font=("Helvetica",18))
        self.pantalla2.grid(row=0,column=4,columnspan=2)
        self.pantalla3=Text(ventana, state="disabled", width=5, height=4, background="black", foreground="white", font=("Helvetica",18))
        self.pantalla3.grid(row=0,column=5,columnspan=3)
        self.pantalla4=Text(ventana, state="disabled", width=5, height=4, background="black", foreground="white", font=("Helvetica",18))
        self.pantalla4.grid(row=0,column=6,columnspan=5)
        self.pantalla5=Text(ventana, state="disabled", width=10, height=4, background="red", foreground="white", font=("Helvetica",18))
        self.pantalla5.grid(row=0,column=8,columnspan=5)
        boton1=self.crearBoton("Q")
        boton2=self.crearBoton("W")
        boton3=self.crearBoton("E")
        boton4=self.crearBoton("R")
        boton5=self.crearBoton("T")
        boton6=self.crearBoton("Y")
        boton7=self.crearBoton("U")
        boton8=self.crearBoton("I")
        boton9=self.crearBoton("O")
        boton10=self.crearBoton("P")
        boton11=self.crearBoton("A")
        boton12=self.crearBoton("S")
        boton13=self.crearBoton("D")
        boton14=self.crearBoton("F")
        boton15=self.crearBoton("G")
        boton16=self.crearBoton("H")
        boton17=self.crearBoton("J")
        boton18=self.crearBoton("K")
        boton19=self.crearBoton("L")
        boton20=self.crearBoton("Ñ")
        boton21=self.crearBoton("Z")
        boton22=self.crearBoton("X")
        boton23=self.crearBoton("C")
        boton24=self.crearBoton("V")
        boton25=self.crearBoton("B")
        boton26=self.crearBoton("N")
        boton27=self.crearBoton("M")
        boton28=self.crearBoton(" ")
        boton29=self.crearBoton(" ")
        boton30=self.crearBoton(" ")
        boton31=self.crearBoton(" ")
        boton32=self.crearBoton(" ")
        boton33=self.crearBoton(" ")
        boton34=self.crearBoton(" ")
        boton35=self.crearBoton(" ")
        boton36=self.crearBoton(" ")
        boton37=self.crearBoton(" ")
        boton38=self.crearBoton(" ")
        boton39=self.crearBoton(" ")
        boton40=self.crearBoton(" ")
        boton41=self.crearBoton(" ")
        
        botones=[boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton10, boton11, boton12, boton13, boton14, boton15, boton16, boton17,boton18, boton19, boton20, boton21, boton22, boton23, boton24, boton25, boton26, boton27, boton28, boton29 ,boton30,boton31,boton32,boton33,boton34,boton35,boton36,boton37,boton38,boton39,boton40,boton41]
        contador=0
        for fila in range(1,4):
            for columna in range(10):
                botones[contador].grid(row=fila,column=columna)
                contador+=1
    def crearBoton(self,valor,escribir=True,ancho=4,alto=4):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Arial Black",20), command=lambda:self.click(valor,escribir))
    def click(self, texto, escribir):
        self.operacion+=str(texto)
        self.mostrarEnPantalla(texto)
        
        
        return
    
    



    def mostrarEnPantalla(self, valor):
        def eliminar1():
            ventana_principal.destroy()
        punto1=0
        punto2=False
        punto3=False
        punto4=False
        if self.puntaje1==4:
            self.pantalla5.configure(state="normal")
            self.pantalla5.insert(END,self.mensaje1)
            self.pantalla5.configure(state="disabled")
            ventana_principal.after(2000,eliminar1)
            
            
        if valor==letra1:
            self.pantalla1.configure(state="normal")
            self.pantalla1.insert(END, valor)
            self.pantalla1.configure(state="disabled")
            self.puntaje1=self.puntaje1+1
            self.pantalla1=False
            return
        elif valor==letra2:
            self.pantalla2.configure(state="normal")
            self.pantalla2.insert(END,valor)
            self.pantalla2.configure(state="disable")
            self.puntaje1=self.puntaje1+1
            self.pantalla2=False
        
        elif valor==letra3 and punto3==False:
            self.pantalla3.configure(state="normal")
            self.pantalla3.insert(END,valor)
            self.pantalla3.configure(state="disable")
            self.puntaje1=self.puntaje1+1
            self.pantalla3=False
        elif  valor==letra4 and punto4==False:

            self.pantalla4.configure(state="normal")
            self.pantalla4.insert(END,valor)
            self.pantalla4.configure(state="disable")
            self.puntaje1=self.puntaje1+1
            self.pantalla4=False
        else:
            self.puntaje=self.puntaje-1
            self.pantalla0.configure(state="normal")
            self.pantalla0.insert(END,self.puntaje)
            self.pantalla0.configure(state="disabled")
            if self.puntaje==-1:
                ventana_principal.destroy()
            elif self.puntaje<1:
                self.pantalla0.configure(state="normal")
                self.pantalla0.insert(END,self.mensaje)
                self.pantalla0.configure(state="disabled")     
            


            


        return


ventana_principal = Tk()
calculadora = Interfaz(ventana_principal)
palabra="GATO"
letra1=palabra[0:1]
letra2=palabra[1:2]
letra3=palabra[2:3]
letra4=palabra[3:4]
ventana_principal.resizable(0,0)
ventana_principal.config(bg="sky blue")
ventana_principal.mainloop()