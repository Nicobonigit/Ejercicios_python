from tkinter import *

def click_boton():
    Label(root, text="Apreto boton").grid(row=2, column=3)
    marco_principal.config(bg="light green")


root = Tk()

marco_principal = Frame()
marco_principal.grid(row=0, column=0)
marco_principal.config(width="100", height="100", bg="red")

marco_principal1 = Frame()
marco_principal1.grid(row=1, column=0)
marco_principal1.config(width="100", height="100", bg="blue")

marco_principal2 = Frame()
marco_principal2.grid(row=2, column=0)
marco_principal2.config(width="100", height="100", bg="yellow")

marco_principal3 = Frame()
marco_principal3.grid(row=0, column=1)
marco_principal3.config(width="100", height="100", bg="green")

marco_principal4 = Frame()
marco_principal4.grid(row=1, column=1)
marco_principal4.config(width="100", height="100", bg="black")

marco_principal5 = Frame()
marco_principal5.grid(row=2, column=10)
marco_principal5.config(width="100", height="100", bg="purple")

marco_principal6 = Frame()
marco_principal6.grid(row=2, column=3)
marco_principal6.config(width="100", height="100")

boton1 = Button(root, text="Apreta", padx=100, pady=25, bg="light blue", fg="white", command=click_boton)
boton1.grid(row=1, column=2)

root.mainloop()
