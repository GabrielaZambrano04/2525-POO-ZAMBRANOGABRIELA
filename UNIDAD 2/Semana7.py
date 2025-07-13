
class Archivo:
    def __init__(self, nombre_archivo):
        # Constructor: se ejecuta cuando se crea un objeto de la clase
        self.nombre_archivo = nombre_archivo
        self.archivo = open(nombre_archivo, 'w')  # Simula abrir un archivo para escribir
        print(f"[Constructor] Archivo '{self.nombre_archivo}' ha sido abierto para escritura.")

    def escribir(self, texto):
        # Método que escribe texto en el archivo
        self.archivo.write(texto)
        print(f"[Acción] Se escribió en el archivo: {texto}")

    def __del__(self):
        # Destructor: se ejecuta automáticamente cuando el objeto es eliminado o el programa finaliza
        self.archivo.close()
        print(f"[Destructor] Archivo '{self.nombre_archivo}' ha sido cerrado correctamente.")

# Uso del programa
if __name__ == "__main__":
    # Crear un objeto de la clase Archivo
    archivo1 = Archivo("gabby.txt")

    # Escribir en el archivo
    archivo1.escribir("Hola, este es un ejemplo de uso de constructores y destructores en Python.\n")

    # El objeto será destruido automáticamente al final del programa o se puede forzar con 'del'
    del archivo1  # Esto invoca explícitamente el destructor
