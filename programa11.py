from tkinter import *

def dividir():
    resultado = round(
        float(entrada1.get()) / float(entrada2.get()), 1
    )

    etiqueta_resultado.config(
        text="Resultado: " + str(resultado)
    )

ventana = Tk()
ventana.title("División Decimal")
ventana.geometry("300x200")

Label(ventana, text="Introduce el dividendo").pack()
entrada1 = Entry(ventana)
entrada1.pack()

Label(ventana, text="Introduce el divisor").pack()
entrada2 = Entry(ventana)
entrada2.pack()

Button(ventana, text="Dividir", command=dividir).pack()

etiqueta_resultado = Label(ventana, text="")
etiqueta_resultado.pack()

ventana.mainloop()
