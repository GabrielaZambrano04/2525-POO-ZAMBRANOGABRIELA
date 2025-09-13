import tkinter as tk
from tkinter import messagebox

# -------------------------------------------
# Aplicación GUI Básica - Tkinter
# Autor: Gabriela Zambrano
# Descripción: Aplicación que permite ingresar
#              datos en una lista usando Tkinter.
# -------------------------------------------

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Gabriela")
ventana.geometry("400x300")

# Etiqueta descriptiva
label = tk.Label(ventana, text="Ingrese un dato:", font=("Arial", 12))
label.pack(pady=5)

# Campo de texto
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# Lista para mostrar datos ingresados
lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=10)

# Función para agregar datos a la lista
def agregar():
    dato = entrada.get()
    if dato.strip() != "":     # Validar que no esté vacío
        lista.insert(tk.END, dato)
        entrada.delete(0, tk.END)  # Limpiar el campo después de agregar
    else:
        messagebox.showwarning("Advertencia", "Debe ingresar un dato.")

# Función para limpiar datos
def limpiar():
    lista.delete(0, tk.END)    # Borra todos los elementos de la lista
    entrada.delete(0, tk.END)  # Limpia el campo de entrada

# Botón para agregar datos
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar)
btn_agregar.pack(side=tk.LEFT, padx=30, pady=10)

# Botón para limpiar datos
btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
btn_limpiar.pack(side=tk.RIGHT, padx=30, pady=10)

# Ejecutar la aplicación
ventana.mainloop()
