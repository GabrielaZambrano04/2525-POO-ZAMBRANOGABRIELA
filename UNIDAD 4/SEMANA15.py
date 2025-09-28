import tkinter as tk
from tkinter import messagebox

# Función para añadir tarea
def agregar_tarea(event=None):
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía.")

# Función para marcar tarea como completada
def marcar_completada():
    try:
        indice = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(indice)
        # Cambiar visualmente agregando un prefijo ✓ si no está marcado
        if not tarea.startswith("✓ "):
            lista_tareas.delete(indice)
            lista_tareas.insert(indice, f"✓ {tarea}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcarla como completada.")

# Función para eliminar tarea
def eliminar_tarea():
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminarla.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Tareas Gabriela")
ventana.geometry("500x500")

# Entrada de texto para nuevas tareas
entrada_tarea = tk.Entry(ventana, width=30)
entrada_tarea.pack(pady=10)
entrada_tarea.bind("<Return>", agregar_tarea)  # Permitir agregar tarea con Enter

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Añadir Tarea", command=agregar_tarea)
btn_agregar.grid(row=0, column=0, padx=5)

btn_completar = tk.Button(frame_botones, text="Marcar como Completada", command=marcar_completada)
btn_completar.grid(row=0, column=1, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.grid(row=0, column=2, padx=5)

# Listbox para mostrar tareas
lista_tareas = tk.Listbox(ventana, width=50, height=15)
lista_tareas.pack(pady=10)

# Evento opcional: doble clic para marcar como completada
lista_tareas.bind("<Double-Button-1>", lambda event: marcar_completada())

# Ejecutar la ventana
ventana.mainloop()
