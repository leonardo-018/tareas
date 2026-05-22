import tkinter as tk

ventana = tk.Tk()
ventana.title("Diccionario")
ventana.geometry("300x150")

diccionario = {
    "nombre": "Leo",
    "grupo": "2bmpg",
    "calificacion": "10"
}

texto = ""
for clave, valor in diccionario.items():
    texto += f"{clave}: {valor}\n"

tk.Label(ventana, text="Datos del alumno:", font=("Arial", 12, "bold")).pack(pady=10)
tk.Label(ventana, text=texto, font=("Arial", 11), justify="left").pack()

ventana.mainloop()
