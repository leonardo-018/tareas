from tkinter import *

def sumar():
    resultado = float(entrada1.get()) + float(entrada2.get())
    etiqueta_resultado.config(text="Resultado de la suma: " + str(resultado))

ventana = Tk()
ventana.title("Suma Enteros")
ventana.geometry("300x200")

Label(ventana, text="Introduzca el primer sumando").pack()
entrada1 = Entry(ventana)
entrada1.pack()

Label(ventana, text="Introduzca el segundo sumando").pack()
entrada2 = Entry(ventana)
entrada2.pack()

Button(ventana, text="Sumar", command=sumar).pack()

etiqueta_resultado = Label(ventana, text="")
etiqueta_resultado.pack()

ventana.mainloop()
