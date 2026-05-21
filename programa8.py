from tkinter import *

def multiplicar():
    resultado = int(entrada1.get()) * int(entrada2.get())
    etiqueta_resultado.config(text="Resultado de multiplicación: " + str(resultado))

ventana = Tk()
ventana.title("Multiplicación Enteros")
ventana.geometry("300x200")

Label(ventana, text="Introduce el multiplicando").pack()
entrada1 = Entry(ventana)
entrada1.pack()

Label(ventana, text="Introduce el multiplicador").pack()
entrada2 = Entry(ventana)
entrada2.pack()

Button(ventana, text="Multiplicar", command=multiplicar).pack()

etiqueta_resultado = Label(ventana, text="")
etiqueta_resultado.pack()

ventana.mainloop()
