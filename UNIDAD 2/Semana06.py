# Clase base: Libro
class Libro:
    def __init__(self, titulo, autor, disponible=True):
        # Atributos encapsulados (privados)
        self.__titulo = titulo
        self.__autor = autor
        self.__disponible = disponible

    # Métodos getter y setter (encapsulación)
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def esta_disponible(self):
        return self.__disponible

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            print(f'El libro "{self.__titulo}" ha sido prestado.')
        else:
            print(f'El libro "{self.__titulo}" no está disponible.')

    def devolver(self):
        self.__disponible = True
        print(f'El libro "{self.__titulo}" ha sido devuelto.')

    # Método que será sobrescrito (polimorfismo)
    def mostrar_informacion(self):
       print(f'Título: {self.get_titulo()}\nAutor: {self.get_autor()}')


# Clase derivada: Libro Físico (Hereda de Libro)
class LibroFisico(Libro):
    def __init__(self, titulo, autor, ubicacion_estante):
        super().__init__(titulo, autor)
        self.ubicacion_estante = ubicacion_estante

    # Polimorfismo: método sobrescrito
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Tipo: Físico\nUbicación: Estante {self.ubicacion_estante}')
        print('-' * 40)


# Clase derivada: Libro Digital (Hereda de Libro)
class LibroDigital(Libro):
    def __init__(self, titulo, autor, url_descarga):
        super().__init__(titulo, autor)
        self.url_descarga = url_descarga

    # Polimorfismo: método sobrescrito
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Tipo: Digital\nDescargar en: {self.url_descarga}')
        print('-' * 40)


# Uso del sistema (Instancias y pruebas)

# Crear objetos
libro1 = LibroFisico("Cien Años de Soledad", "Gabriel García Márquez", "A3")
libro2 = LibroDigital("Python para Principiantes", "Ana Pérez", "https://ejemplo.com/python")

# Mostrar información (demostración de polimorfismo)
libro1.mostrar_informacion()
libro2.mostrar_informacion()

# Usar métodos encapsulados
libro1.prestar()
libro1.prestar()  # intenta prestarlo otra vez
libro1.devolver()
libro1.prestar()