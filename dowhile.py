import tkinter as tk
from tkinter import messagebox

def ejecutar():
    while True:
        messagebox.showinfo("Saludo", "¡Hola!")
        respuesta = messagebox.askyesno("Repetir", "¿Quieres repetir?")
        if respuesta == False:
            break

ventana = tk.Tk()
ventana.title("Do While Simulado")
ventana.geometry("250x100")

tk.Button(ventana, text="Iniciar ciclo", command=ejecutar).pack(pady=30)
ventana.mainloop()
