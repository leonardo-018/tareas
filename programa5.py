from tkinter import *

def restar():
    resultado = int(entrada1.get()) - int(entrada2.get())
    etiqueta_resultado.config(text="Resultado de resta: " + str(resultado))

ventana = Tk()
ventana.title("Resta Enteros")
ventana.geometry("300x200")

Label(ventana, text="Introduzca el minuendo").pack()
entrada1 = Entry(ventana)
entrada1.pack()

Label(ventana, text="Introduzca el sustraendo").pack()
entrada2 = Entry(ventana)
entrada2.pack()

Button(ventana, text="Restar", command=restar).pack()

etiqueta_resultado = Label(ventana, text="")
etiqueta_resultado.pack()

ventana.mainloop()
