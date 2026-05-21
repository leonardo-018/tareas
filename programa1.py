from tkinter import *

ventana = Tk()
ventana.title("Programa 1")
ventana.geometry("300x200")

label1 = Label(ventana, text="Hola Time of Software")
label1.pack()

label2 = Label(ventana, text="Este es mi primer programa con Python")
label2.pack()

ventana.mainloop()
