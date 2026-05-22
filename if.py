import tkinter as tk
from tkinter import messagebox

def verificar():
        edad = int(entrada.get())
        if edad >= 18:
            messagebox.showinfo("Resultado", "Puedes votar")
        else:
            messagebox.showinfo("Resultado", "No puedes votar")
    

ventana = tk.Tk()
ventana.title("¿Puedes votar?")
ventana.geometry("300x150")

tk.Label(ventana, text="¿Cuántos años tienes?:").pack(pady=10)
entrada = tk.Entry(ventana)
entrada.pack()

tk.Button(ventana, text="Verificar", command=verificar).pack(pady=10)

ventana.mainloop()
