import tkinter as tk

def elegir():
        eleccion = int(entrada.get())
        match eleccion:
            case 1:
                resultado.config(text="Elegiste el #1")
            case 2:
                resultado.config(text="Elegiste el #2")
            case 3:
                resultado.config(text="Elegiste el #3")
            case _:
                resultado.config(text="Opción no válida")

ventana = tk.Tk()
ventana.title("Switch con Match")
ventana.geometry("300x180")

tk.Label(ventana, text="Elige un número del 1 al 3:").pack(pady=10)
entrada = tk.Entry(ventana)
entrada.pack()

tk.Button(ventana, text="Aceptar", command=elegir).pack(pady=5)
resultado = tk.Label(ventana, text="", font=("Arial", 12))
resultado.pack(pady=10)

ventana.mainloop()
