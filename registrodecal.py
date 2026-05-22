print("--- Registro de Calificaciones ---")

alumnos = []

cantidad = input("¿Cuántos alumnos vas a registrar?: ")
cantidad = int(cantidad)

if cantidad <= 0:
    print("Cantidad no válida")
else:
    def pedir_calificacion(numero):
        calificacion = float(input("Calificacion " + str(numero) + ": "))
        
        while calificacion < 0 or calificacion > 10:
            print("Error: debe ser de 0 a 10")
            calificacion = float(input("Captura de nuevo: "))
        
        return calificacion

    for i in range(cantidad):
        print(f"\n--- Alumno {i+1} ---")
        nombre = input("Nombre del alumno: ")
        
        c1 = pedir_calificacion(1)
        c2 = pedir_calificacion(2)
        c3 = pedir_calificacion(3)
        
        promedio = (c1 + c2 + c3) / 3
        
        if promedio >= 6:
            estado = "Aprobado"
        else:
            estado = "Reprobado"
        
        alumnos.append({
            "nombre": nombre,
            "promedio": promedio,
            "estado": estado
        })
        
        print("Alumno registrado")

    print("\n=== RESUMEN FINAL ===")
    for alumno in alumnos:
        print(f"Nombre: {alumno['nombre']} | Promedio: {alumno['promedio']:.2f} | Estado: {alumno['estado']}")
