import tkinter as tk
from tkinter import messagebox

class GestorTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas Gabby")
        self.root.geometry("400x450")
        self.root.config(bg="#f4f4f4")

        # Campo de entrada
        self.entrada = tk.Entry(root, font=("Arial", 12))
        self.entrada.pack(pady=10, padx=10, fill=tk.X)
        self.entrada.focus()

        # Botones
        marco_botones = tk.Frame(root, bg="#f4f4f4")
        marco_botones.pack(pady=5)

        tk.Button(marco_botones, text="➕ Añadir", command=self.agregar_tarea, bg="#4CAF50", fg="white", width=12).grid(row=0, column=0, padx=5)
        tk.Button(marco_botones, text="✔ Completar", command=self.marcar_completada, bg="#2196F3", fg="white", width=12).grid(row=0, column=1, padx=5)
        tk.Button(marco_botones, text="🗑 Eliminar", command=self.eliminar_tarea, bg="#f44336", fg="white", width=12).grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.lista = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE, activestyle="none")
        self.lista.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Vincular atajos de teclado
        self.root.bind("<Return>", lambda event: self.agregar_tarea())       # Enter → Añadir
        self.root.bind("<c>", lambda event: self.marcar_completada())        # C → Completar
        self.root.bind("<d>", lambda event: self.eliminar_tarea())           # D → Eliminar
        self.root.bind("<Delete>", lambda event: self.eliminar_tarea())      # Delete → Eliminar
        self.root.bind("<Escape>", lambda event: self.cerrar_aplicacion())   # Escape → Salir

    def agregar_tarea(self):
        tarea = self.entrada.get().strip()
        if tarea:
            self.lista.insert(tk.END, tarea)
            self.entrada.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Por favor escribe una tarea antes de añadirla.")

    def marcar_completada(self):
        seleccion = self.lista.curselection()
        if not seleccion:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para marcarla como completada.")
            return
        indice = seleccion[0]
        texto = self.lista.get(indice)
        # Verificar si ya está completada
        if texto.startswith("✔ "):
            texto = texto[2:]  # Quitar marca
        else:
            texto = "✔ " + texto  # Agregar marca
        self.lista.delete(indice)
        self.lista.insert(indice, texto)
        # Cambiar color visual
        self.lista.itemconfig(indice, fg="gray" if texto.startswith("✔") else "black")

    def eliminar_tarea(self):
        seleccion = self.lista.curselection()
        if not seleccion:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para eliminar.")
            return
        self.lista.delete(seleccion[0])

    def cerrar_aplicacion(self):
        if messagebox.askokcancel("Salir", "¿Deseas cerrar la aplicación?"):
            self.root.destroy()


# Ejecución principal
if __name__ == "__main__":
    root = tk.Tk()
    app = GestorTareas(root)
    root.mainloop()
