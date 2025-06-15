# Clase padre que representa un registro climático genérico
class RegistroClimatico:
    def __init__(self, dia):
        self.dia = dia

    def obtener_valor(self):
       return 0

# Clase hija que representa un registro de temperatura
class Temperatura(RegistroClimatico):
    def __init__(self, dia, temperatura):
        super().__init__(dia)        # Hereda el atributo dia
        self.temperatura = temperatura

    def obtener_valor(self):
        return self.temperatura

# Clase que gestiona una semana de temperaturas
class TemperaturaSemana:
    def __init__(self):
        self.dias = []

    def agregar_dia(self, registro_climatico):
        self.dias.append(registro_climatico)

    def calcular_promedio(self):
        if len(self.dias) == 0:
            return 0
        total = sum([dia.obtener_valor() for dia in self.dias])       # Método polimórfico
        return total / len(self.dias)

# Uso del programa fuera de las clases
semana = TemperaturaSemana()
semana.agregar_dia(Temperatura("lunes", 25.2))
semana.agregar_dia(Temperatura("martes", 22.4))
semana.agregar_dia(Temperatura("miércoles", 32.4))
semana.agregar_dia(Temperatura("jueves", 33.3))
semana.agregar_dia(Temperatura("viernes", 29.6))
semana.agregar_dia(Temperatura("sábado", 27.8))
semana.agregar_dia(Temperatura("domingo", 30.3))

promedio = semana.calcular_promedio()
print(f"Temperatura promedio semanal: {promedio:.2f}°C")