from tkinter import *

ventana = Tk()
ventana.title("Cadena")
ventana.geometry("300x200")

cadenaEjemplo = "Hola Time of Software"

label = Label(ventana, text=cadenaEjemplo)
label.pack()

ventana.mainloop()
