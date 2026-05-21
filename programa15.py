from tkinter import *

ventana = Tk()
ventana.title("Lista")
ventana.geometry("300x200")

lista = ["ordenador", "teclado", "raton"]

label = Label(ventana, text=str(lista))
label.pack()

ventana.mainloop()
