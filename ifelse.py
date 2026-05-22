import tkinter as tk
from tkinter import messagebox

def verificar():
        edad = int(entrada.get())
        if edad >= 18:
            resultado.config(text="Eres mayor de edad")
        else:
            resultado.config(text="Eres menor de edad")

ventana = tk.Tk()
ventana.title("Mayor de edad")
ventana.geometry("300x150")

tk.Label(ventana, text="Introduce tu edad:").pack(pady=10)
entrada = tk.Entry(ventana)
entrada.pack()

tk.Button(ventana, text="Verificar", command=verificar).pack(pady=5)
resultado = tk.Label(ventana, text="", font=("Arial", 12))
resultado.pack(pady=10)

ventana.mainloop()
