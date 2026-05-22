import tkinter as tk

def mostrar():
    ventana_saludo = tk.Toplevel(ventana)
    ventana_saludo.title("Saludo")
    tk.Label(ventana_saludo, text="¡Hola!", font=("Arial", 20)).pack(padx=20, pady=20)

ventana = tk.Tk()
ventana.title("While con Botón")
ventana.geometry("300x120")

tk.Label(ventana, text="¿Quieres mostrar un mensaje?").pack(pady=10)
tk.Button(ventana, text="Sí, mostrar", command=mostrar).pack()
tk.Button(ventana, text="Salir", command=ventana.quit).pack(pady=5)

ventana.mainloop()
