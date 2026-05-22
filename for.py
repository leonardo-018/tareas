import tkinter as tk
from tkinter import messagebox

def agregar_numero():
        num = int(entrada_num.get())
        numeros.append(num)
        lista_numeros.config(text=f"Números: {numeros}")
        entrada_num.delete(0, tk.END)

def calcular_suma():
    total = sum(numeros)
    resultado.config(text=f"La suma es: {total}")

numeros = []

ventana = tk.Tk()
ventana.title("Suma con For")
ventana.geometry("300x250")

tk.Label(ventana, text="Mete un número y dale Agregar:").pack(pady=5)
entrada_num = tk.Entry(ventana)
entrada_num.pack()

tk.Button(ventana, text="Agregar", command=agregar_numero).pack(pady=5)

lista_numeros = tk.Label(ventana, text="Números: []")
lista_numeros.pack(pady=5)

tk.Button(ventana, text="Calcular suma total", command=calcular_suma).pack(pady=10)

resultado = tk.Label(ventana, text="", font=("Arial", 12, "bold"))
resultado.pack(pady=10)

ventana.mainloop()
