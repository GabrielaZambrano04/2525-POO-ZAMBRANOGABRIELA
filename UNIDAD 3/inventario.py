
import os
from producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        """
        Inicializa el inventario.
        Carga los productos desde archivo TXT.
        """
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """
        Carga productos desde archivo TXT.
        Cada línea es: id,nombre,cantidad,precio
        Maneja excepciones: archivo no encontrado o sin permisos.
        """
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                self.productos = []
                for linea in f:
                    linea = linea.strip()
                    if not linea:
                        continue
                    partes = linea.split(",")
                    if len(partes) != 4:
                        print(f"Línea inválida ignorada: {linea}")
                        continue
                    id_p, nombre, cantidad, precio = partes
                    prod = Producto(int(id_p), nombre, int(cantidad), float(precio))
                    self.productos.append(prod)
            print(f"Inventario cargado desde {self.archivo}.")
        except FileNotFoundError:
            print(f"Archivo {self.archivo} no encontrado. Se creará uno nuevo al guardar.")
            self.productos = []
        except PermissionError:
            print(f"Error: No tienes permisos para leer {self.archivo}. Inventario vacío.")
            self.productos = []

    def guardar_en_archivo(self):
        """
        Guarda los productos en archivo TXT.
        Cada línea es: id,nombre,cantidad,precio
        """
        tmp = self.archivo + ".tmp"
        try:
            with open(tmp, "w", encoding="utf-8") as f:
                for p in self.productos:
                    f.write(f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n")
            os.replace(tmp, self.archivo)
            print("Inventario guardado correctamente.")
        except PermissionError:
            if os.path.exists(tmp):
                os.remove(tmp)
            print(f"Error: No tienes permisos para escribir en {self.archivo}.")
        except Exception as e:
            if os.path.exists(tmp):
                os.remove(tmp)
            print("Error inesperado al guardar:", e)

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: El ID ya existe, no se puede agregar el producto.")
                return
        self.productos.append(producto)
        print("Producto agregado con éxito.")
        self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado.")
                self.guardar_en_archivo()
                return
        print("No se encontró el producto con ese ID.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("Producto actualizado.")
                self.guardar_en_archivo()
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)
