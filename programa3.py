from tkinter import *

ventana = Tk()
ventana.title("Programa 3")
ventana.geometry("300x200")

texto = "1 / 2 / 3 / 4 / 5."

label = Label(ventana, text=texto)
label.pack()

ventana.mainloop()
