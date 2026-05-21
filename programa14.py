from tkinter import *

ventana = Tk()
ventana.title("Cadena")
ventana.geometry("300x200")

cadenaEjemplo = "Hola Time of Software\nEsto es una cadena\nmultilinea"

label = Label(ventana, text=cadenaEjemplo)
label.pack()

ventana.mainloop()
