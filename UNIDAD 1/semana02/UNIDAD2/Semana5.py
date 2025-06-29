# Programa: Calculadora de área de figuras geométricas con datos definidos
# Funcionalidad: Calcula el área de un círculo, cuadrado y triángulo usando datos predefinidos

import math

# Función para calcular el área de un círculo
def calcular_area_circulo(radio: float) -> float:
    return math.pi * radio ** 2

# Función para calcular el área de un cuadrado
def calcular_area_cuadrado(lado: float) -> float:
    return lado ** 2

# Función para calcular el área de un triángulo
def calcular_area_triangulo(base: float, altura: float) -> float:
    return (base * altura) / 2

# Datos definidos para las figuras
radio_circulo: float = 5.0  # en cm
lado_cuadrado: float = 4.0  # en cm
base_triangulo: float = 6.0  # en cm
altura_triangulo: float = 3.0  # en cm

# Cálculos
area_circulo: float = calcular_area_circulo(radio_circulo)
area_cuadrado: float = calcular_area_cuadrado(lado_cuadrado)
area_triangulo: float = calcular_area_triangulo(base_triangulo, altura_triangulo)

# Resultados
print("Áreas calculadas con valores predefinidos:\n")
print(f"Radio del círculo: {radio_circulo} cm → Área: {area_circulo:.2f} cm²")
print(f"Lado del cuadrado: {lado_cuadrado} cm → Área: {area_cuadrado:.2f} cm²")
print(f"Base del triángulo: {base_triangulo} cm, Altura: {altura_triangulo} cm → Área: {area_triangulo:.2f} cm²")

