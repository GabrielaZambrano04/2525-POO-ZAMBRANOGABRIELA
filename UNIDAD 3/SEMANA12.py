# =====================================
# Sistema de Gestión de Biblioteca Digital con Menú Interactivo
# =====================================

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.datos = (titulo, autor)  # Tupla inmutable (título, autor)
        self.categoria = categoria
        self.isbn = isbn

    @property
    def titulo(self):
        return self.datos[0]

    @property
    def autor(self):
        return self.datos[1]

    def __str__(self):
        return f"[{self.isbn}] {self.titulo} - {self.autor} ({self.categoria})"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"


class Biblioteca:
    def __init__(self):
        self.libros = {}        # Diccionario {ISBN: Libro}
        self.usuarios = {}      # Diccionario {ID: Usuario}
        self.ids_usuarios = set()  # Conjunto de IDs únicos

    # --------------------
    # Gestión de libros
    # --------------------
    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print("Este libro ya existe en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro agregado: {libro}")

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            eliminado = self.libros.pop(isbn)
            print(f"Libro eliminado: {eliminado}")
        else:
            print("No se encontró el libro con ese ISBN.")

    # --------------------
    # Gestión de usuarios
    # --------------------
    def registrar_usuario(self, usuario):
        if usuario.user_id in self.ids_usuarios:
            print("El ID de usuario ya está registrado.")
        else:
            self.usuarios[usuario.user_id] = usuario
            self.ids_usuarios.add(usuario.user_id)
            print(f"Usuario registrado: {usuario}")

    def dar_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            eliminado = self.usuarios.pop(user_id)
            self.ids_usuarios.remove(user_id)
            print(f"Usuario eliminado: {eliminado}")
        else:
            print("No se encontró el usuario con ese ID.")

    # --------------------
    # Préstamos
    # --------------------
    def prestar_libro(self, user_id, isbn):
        if user_id not in self.usuarios:
            print("Usuario no encontrado.")
            return
        if isbn not in self.libros:
            print("Libro no disponible en la biblioteca.")
            return

        usuario = self.usuarios[user_id]
        libro = self.libros.pop(isbn)
        usuario.libros_prestados.append(libro)
        print(f"Libro prestado: {libro} a {usuario.nombre}")

    def devolver_libro(self, user_id, isbn):
        if user_id not in self.usuarios:
            print("Usuario no encontrado.")
            return

        usuario = self.usuarios[user_id]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros[isbn] = libro
                print(f"Libro devuelto: {libro}")
                return
        print("El usuario no tiene prestado ese libro.")

    # --------------------
    # Búsquedas
    # --------------------
    def buscar_por_titulo(self, titulo):
        return [libro for libro in self.libros.values() if titulo.lower() in libro.titulo.lower()]

    def buscar_por_autor(self, autor):
        return [libro for libro in self.libros.values() if autor.lower() in libro.autor.lower()]

    def buscar_por_categoria(self, categoria):
        return [libro for libro in self.libros.values() if categoria.lower() == libro.categoria.lower()]

    # --------------------
    # Listar préstamos
    # --------------------
    def listar_prestamos(self, user_id):
        if user_id not in self.usuarios:
            print("Usuario no encontrado.")
            return
        usuario = self.usuarios[user_id]
        if usuario.libros_prestados:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(f"  - {libro}")
        else:
            print(f"{usuario.nombre} no tiene libros prestados.")


# =====================================
# Menú Interactivo
# =====================================
def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n===== MENÚ BIBLIOTECA DIGITAL =====")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro por título")
        print("8. Buscar libro por autor")
        print("9. Buscar libro por categoría")
        print("10. Listar libros prestados de un usuario")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            isbn = input("ISBN del libro a eliminar: ")
            biblioteca.eliminar_libro(isbn)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            user_id = input("ID único del usuario: ")
            usuario = Usuario(nombre, user_id)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":
            user_id = input("ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(user_id)

        elif opcion == "5":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(user_id, isbn)

        elif opcion == "6":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(user_id, isbn)

        elif opcion == "7":
            titulo = input("Título del libro a buscar: ")
            resultados = biblioteca.buscar_por_titulo(titulo)
            print("Resultados de la búsqueda:")
            for libro in resultados:
                print(libro)

        elif opcion == "8":
            autor = input("Autor del libro a buscar: ")
            resultados = biblioteca.buscar_por_autor(autor)
            print("Resultados de la búsqueda:")
            for libro in resultados:
                print(libro)

        elif opcion == "9":
            categoria = input("Categoría del libro a buscar: ")
            resultados = biblioteca.buscar_por_categoria(categoria)
            print("Resultados de la búsqueda:")
            for libro in resultados:
                print(libro)

        elif opcion == "10":
            user_id = input("ID del usuario: ")
            biblioteca.listar_prestamos(user_id)

        elif opcion == "0":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


# =====================================
# Ejecutar programa
# =====================================
if __name__ == "__main__":
    menu()

