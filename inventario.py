print("--- Inventario ---")

inventario = {}

def agregar_producto(nombre, cantidad):
    inventario[nombre] = cantidad
    print("Producto ingresado")

opcion = 0

while opcion!= 4:
    print("\n1. Agregar producto")
    print("2. Vender producto")
    print("3. Mostrar inventario")
    print("4. Salir")

    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        nombre = input("Producto: ")
        cantidad = int(input("Cantidad: "))
        agregar_producto(nombre, cantidad)
    
    elif opcion == 2:
        nombre = input("Producto vendido: ")
        cantidad = int(input("Cantidad vendida: "))
        
        if nombre in inventario and inventario[nombre] >= cantidad:
            inventario[nombre] = inventario[nombre] - cantidad
        else:
            print("No hay suficiente producto")
    
    elif opcion == 3:
        for producto, cantidad in inventario.items():
            print(producto, cantidad)

print("Programa terminado")
