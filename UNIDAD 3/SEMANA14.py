import tkinter as tk
from tkinter import ttk, messagebox
import calendar
import datetime
import json
import os

EVENTS_FILE = "events.json"


# ---------------------------
# DatePicker (Toplevel)
# ---------------------------
class DatePicker(tk.Toplevel):
    def __init__(self, parent, callback, year=None, month=None):
        super().__init__(parent)
        self.callback = callback
        self.transient(parent)
        self.grab_set()
        self.title("Seleccionar fecha")

        today = datetime.date.today()
        self.year = year or today.year
        self.month = month or today.month

        self._build_widget()
        self._update_calendar()

    def _build_widget(self):
        header = tk.Frame(self)
        header.pack(pady=5, padx=5)

        tk.Button(header, text="<", width=3, command=self._prev_month).pack(side="left")
        self.lbl = tk.Label(header, text="", width=18)
        self.lbl.pack(side="left", padx=5)
        tk.Button(header, text=">", width=3, command=self._next_month).pack(side="left")

        cal_frame = tk.Frame(self)
        cal_frame.pack(padx=5, pady=5)

        # Cabecera días (Lun..Dom)
        days = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
        for i, d in enumerate(days):
            tk.Label(cal_frame, text=d, width=4).grid(row=0, column=i)

        # Botones para días
        self.day_buttons = []
        for r in range(1, 7):
            row = []
            for c in range(7):
                b = tk.Button(cal_frame, text="", width=4, state="disabled")
                b.grid(row=r, column=c, padx=1, pady=1)
                row.append(b)
            self.day_buttons.append(row)

        btns = tk.Frame(self)
        btns.pack(pady=5)
        tk.Button(btns, text="Cancelar", command=self.destroy).pack()

    def _update_calendar(self):
        self.lbl.config(text=f"{calendar.month_name[self.month]} {self.year}")
        monthcal = calendar.monthcalendar(self.year, self.month)
        for r in range(6):
            week = monthcal[r] if r < len(monthcal) else [0]*7
            for c in range(7):
                day = week[c]
                btn = self.day_buttons[r][c]
                if day == 0:
                    btn.config(text="", state="disabled", command=lambda: None)
                else:
                    # fijamos 'day' por defecto en lambda para capturarlo correctamente
                    btn.config(text=str(day), state="normal",
                               command=lambda d=day: self._select_day(d))

    def _select_day(self, day):
        fecha = f"{day:02d}/{self.month:02d}/{self.year}"
        self.callback(fecha)
        self.destroy()

    def _prev_month(self):
        self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1
        self._update_calendar()

    def _next_month(self):
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
        self._update_calendar()


# Funciones de utilidad

def validar_fecha(fecha_str):
    try:
        datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
        return True
    except Exception:
        return False


def validar_hora(hora_str):
    # Formato HH:MM, 24 horas
    try:
        parts = hora_str.split(":")
        if len(parts) != 2:
            return False
        hh = int(parts[0])
        mm = int(parts[1])
        return 0 <= hh <= 23 and 0 <= mm <= 59
    except Exception:
        return False


def cargar_eventos(tree):
    if not os.path.exists(EVENTS_FILE):
        return
    try:
        with open(EVENTS_FILE, "r", encoding="utf-8") as f:
            eventos = json.load(f)
        for ev in eventos:
            tree.insert("", "end", values=(ev["fecha"], ev["hora"], ev["descripcion"]))
    except Exception:
        messagebox.showwarning("Carga eventos", "No se pudo cargar events.json (archivo corrupto?)")


def guardar_eventos(tree):
    eventos = []
    for iid in tree.get_children():
        fecha, hora, desc = tree.item(iid)["values"]
        eventos.append({"fecha": fecha, "hora": hora, "descripcion": desc})
    try:
        with open(EVENTS_FILE, "w", encoding="utf-8") as f:
            json.dump(eventos, f, ensure_ascii=False, indent=2)
    except Exception as e:
        messagebox.showerror("Guardar eventos", f"No se pudo guardar: {e}")


# Interfaz principal

def main():
    root = tk.Tk()
    root.title("EVENTOS DE GABRIELA 2025")
    root.geometry("760x420")

    # Frame lista (TreeView)
    frame_lista = tk.Frame(root)
    frame_lista.pack(fill="both", expand=True, padx=10, pady=8)

    tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings", height=9)
    tree.heading("Fecha", text="Fecha")
    tree.heading("Hora", text="Hora")
    tree.heading("Descripción", text="Descripción")
    tree.column("Fecha", width=100)
    tree.column("Hora", width=80)
    tree.column("Descripción", width=520)
    tree.pack(side="left", fill="both", expand=True)

    scroll = ttk.Scrollbar(frame_lista, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scroll.set)
    scroll.pack(side="right", fill="y")

    # Frame formulario
    frame_form = tk.Frame(root)
    frame_form.pack(fill="x", padx=10, pady=6)

    tk.Label(frame_form, text="Fecha:").grid(row=0, column=0, padx=5, pady=4)
    var_fecha = tk.StringVar()
    entry_fecha = tk.Entry(frame_form, textvariable=var_fecha, width=12)
    entry_fecha.grid(row=0, column=1, padx=5, pady=4)

    # Botón que abre el DatePicker propio
    tk.Button(frame_form, text="📅", command=lambda: DatePicker(root, lambda d: var_fecha.set(d))).grid(row=0, column=2)

    tk.Label(frame_form, text="Hora (HH:MM):").grid(row=0, column=3, padx=5, pady=4)
    entry_hora = tk.Entry(frame_form, width=10)
    entry_hora.grid(row=0, column=4, padx=5, pady=4)

    tk.Label(frame_form, text="Descripción:").grid(row=0, column=5, padx=5, pady=4)
    entry_desc = tk.Entry(frame_form, width=40)
    entry_desc.grid(row=0, column=6, padx=5, pady=4)

    # Frame botones
    frame_btn = tk.Frame(root)
    frame_btn.pack(fill="x", padx=10, pady=8)

    def agregar_evento():
        fecha = var_fecha.get().strip()
        hora = entry_hora.get().strip()
        desc = entry_desc.get().strip()

        if not fecha or not hora or not desc:
            messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
            return
        if not validar_fecha(fecha):
            messagebox.showerror("Fecha inválida", "La fecha debe tener formato DD/MM/AAAA.")
            return
        if not validar_hora(hora):
            messagebox.showerror("Hora inválida", "La hora debe tener formato HH:MM (00:00 - 23:59).")
            return

        tree.insert("", "end", values=(fecha, hora, desc))
        guardar_eventos(tree)

        # limpiar
        entry_hora.delete(0, "end")
        entry_desc.delete(0, "end")
        var_fecha.set("")

    def eliminar_evento():
        sel = tree.selection()
        if not sel:
            messagebox.showwarning("Eliminar", "Selecciona al menos un evento para eliminar.")
            return
        if messagebox.askyesno("Confirmar", "¿Deseas eliminar el/los evento(s) seleccionado(s)?"):
            for iid in sel:
                tree.delete(iid)
            guardar_eventos(tree)

    tk.Button(frame_btn, text="Agregar Evento", command=agregar_evento).pack(side="left", padx=8)
    tk.Button(frame_btn, text="Eliminar Evento Seleccionado", command=eliminar_evento).pack(side="left", padx=8)
    tk.Button(frame_btn, text="Salir", command=root.quit).pack(side="right", padx=8)

    # cargar eventos previos
    cargar_eventos(tree)

    root.mainloop()


if __name__ == "__main__":
    main()

