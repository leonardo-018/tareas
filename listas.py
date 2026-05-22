import tkinter as tk
from tkinter import messagebox

nombres = ["Juan", "María", "Ignacio"]

def mostrar_nombre():
    try:
        eleccion = int(entrada.get())
        if 0 <= eleccion < len(nombres):
            resultado.config(text=f"Elegiste: {nombres[eleccion]}")
        else:
            resultado.config(text=f"Usa un número del 0 al {len(nombres)-1}")
    except ValueError:
        messagebox.showerror("Error", "Ingresa un número válido")

ventana = tk.Tk()
ventana.title("Lista de Nombres")
ventana.geometry("300x180")

tk.Label(ventana, text=f"Elige un número del 0 al {len(nombres)-1}").pack(pady=10)
tk.Label(ventana, text=f"Nombres: {nombres}").pack()

entrada = tk.Entry(ventana)
entrada.pack(pady=5)

tk.Button(ventana, text="Mostrar", command=mostrar_nombre).pack(pady=5)
resultado = tk.Label(ventana, text="", font=("Arial", 12, "bold"))
resultado.pack(pady=10)

ventana.mainloop()
