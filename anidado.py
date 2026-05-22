import tkinter as tk
from tkinter import messagebox

def evaluar():
        cal = int(entrada.get())
        if cal == 10:
            texto = "Excelente"
        elif cal == 9:
            texto = "Bueno"
        elif cal == 8:
            texto = "Bien"
        elif cal == 7:
            texto = "Más o menos"
        elif cal == 6:
            texto = "Suficiente"
        elif cal <= 5:
            texto = "Necesitas mejorar"
        else:
            texto = "Calificación inválida"
        resultado.config(text=texto)

ventana = tk.Tk()
ventana.title("Evaluador de Calificación")
ventana.geometry("300x180")

tk.Label(ventana, text="Introduce tu calificación:").pack(pady=10)
entrada = tk.Entry(ventana)
entrada.pack()

tk.Button(ventana, text="Evaluar", command=evaluar).pack(pady=5)
resultado = tk.Label(ventana, text="", font=("Arial", 12, "bold"))
resultado.pack(pady=10)

ventana.mainloop()
