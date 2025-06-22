# Clase Dueño
class Dueño:
    def __init__(self, nombre, telefono):
        self.nombre=nombre
        self.telefono=telefono


# Clase mascota
class mascota:
    def __init__(self,nombre, edad, dueño):
       self.nombre=nombre
       self.edad=edad
       self.dueño=dueño
       
    def presentarse (self):
        return f"soy {self.nombre}, tengo {self.edad} años"
    
#Subclase que hereda mascota
class Gato(mascota):
    def hacer_sonido(self):
        return "miau!"

class Perro(mascota):
    def hacer_sonido(self):
        return "Guau!"

# Clase visita medica
class visitamedica:
    def __init__(self, mascota, diagnostico):
        self.mascota=mascota
        self.diagnostico=diagnostico
    
    def resumen_visita(self):
        return f"visita de {self.mascota.nombre}: {self.diagnostico}"
    
    # Crear dueño
    dueño1= Dueño("Gabriela Zambrano","0979773389")
    
# Crear mascota
gato1= Gato("princesa", 2 ,"dueño1")
perro1=Perro("Jac", 5 ,"dueño1")

# Mostrar sonidos
print(gato1.presentarse(),gato1.hacer_sonido())
print(perro1.presentarse(),perro1.hacer_sonido())

# Registrar visita medica
visita=visitamedica(perro1,"vacunación anual realizada.")
print(visita.resumen_visita())