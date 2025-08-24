# main.py
from inventario import Inventario
from producto import Producto

def menu():
    inventario = Inventario()

    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                id_p = int(input("ID del producto: "))
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                prod = Producto(id_p, nombre, cantidad, precio)
                inventario.agregar_producto(prod)
                print(f"Producto '{nombre}' agregado y guardado en {inventario.archivo}.")
            except ValueError:
                print("Error: Debes ingresar datos válidos.")

        elif opcion == "2":
            try:
                id_p = int(input("ID del producto a eliminar: "))
                inventario.eliminar_producto(id_p)
                print(f"Intento de eliminación registrado en {inventario.archivo}.")
            except ValueError:
                print("Error: ID inválido.")

        elif opcion == "3":
            try:
                id_p = int(input("ID del producto a actualizar: "))
                nueva_cantidad = input("Nueva cantidad (ENTER para no cambiar): ")
                nuevo_precio = input("Nuevo precio (ENTER para no cambiar): ")

                nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
                nuevo_precio = float(nuevo_precio) if nuevo_precio else None

                inventario.actualizar_producto(id_p, nueva_cantidad, nuevo_precio)
                print(f"Intento de actualización registrado en {inventario.archivo}.")
            except ValueError:
                print("Error: Ingresa valores numéricos válidos.")

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                print(f"Se encontraron {len(resultados)} producto(s) con '{nombre}':")
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            inventario.mostrar_productos()
            print(f"Inventario actual mostrado desde {inventario.archivo}.")

        elif opcion == "6":
            print("Saliendo del sistema... ¡Hasta pronto!")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
