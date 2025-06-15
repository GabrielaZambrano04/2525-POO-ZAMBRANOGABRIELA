#Lista de temperaturas 
temperaturas= [25.2, 22.4, 32.4, 33.3, 29.6, 27.8,30.3,]

# Funcion para calcular el promedio
def calcular_promedio(lista):
    return sum(lista) / len(lista)

# Llamar a la funcion y mostrar el resultado
promedio= calcular_promedio(temperaturas)
print(f"temperatura promedio semanal:{promedio:.2f}°c")
