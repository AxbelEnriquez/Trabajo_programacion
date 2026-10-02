import tkinter as tk


class CalculadoraTkinter:

  def __init__(self, root):
    self.root = root
    self.root.title("Calculadora 3 - Tkinter")
    self.root.geometry("320x500")  # Corregido aquí
    self.root.resizable(False, False)
    self.root.config(bg="#f0f0f0")

    self.historial = []
    self.crear_interfaz()

  def crear_interfaz(self):
    # Pantalla de la calculadora
    self.pantalla_var = tk.StringVar()
    self.pantalla = tk.Entry(
        self.root,
        textvariable=self.pantalla_var,
        font=("Arial", 20, "bold"),
        justify="right",
        bd=5,
        relief=tk.FLAT,
        bg="#ffffff",
        fg="#333333",
    )
    self.pantalla.pack(fill=tk.X, padx=15, pady=15, ipady=10)

    # Marco para los botones
    marco_botones = tk.Frame(self.root, bg="#f0f0f0")
    marco_botones.pack(padx=15, pady=5)

    botones = [
        ("7", 1, 0),
        ("8", 1, 1),
        ("9", 1, 2),
        ("/", 1, 3),
        ("4", 2, 0),
        ("5", 2, 1),
        ("6", 2, 2),
        ("*", 2, 3),
        ("1", 3, 0),
        ("2", 3, 1),
        ("3", 3, 2),
        ("-", 3, 3),
        ("0", 4, 0),
        ("C", 4, 1),
        ("=", 4, 2),
        ("+", 4, 3),
    ]

    for texto, fila, columna in botones:
      if texto == "C":
        bg_color = "#e74c3c"  # Rojo para borrar
        fg_color = "white"
      elif texto == "=":
        bg_color = "#2ecc71"  # Verde para igual
        fg_color = "white"
      else:
        bg_color = "#e0e0e0"
        fg_color = "#333333"

      btn = tk.Button(
          marco_botones,
          text=texto,
          font=("Arial", 14, "bold"),
          width=5,
          height=2,
          bg=bg_color,
          fg=fg_color,
          relief=tk.RAISED,
          bd=2,
          command=lambda t=texto: self.clic_boton(t),
      )
      btn.grid(row=fila, column=columna, padx=5, pady=5)

    # Sección de Historial
    lbl_historial = tk.Label(
        self.root,
        text="Historial (Últimas operaciones):",
        font=("Arial", 10, "bold"),
        bg="#f0f0f0",
        anchor="w",
    )
    lbl_historial.pack(fill=tk.X, padx=15, pady=(10, 0))

    self.lista_historial = tk.Listbox(
        self.root, font=("Arial", 10), height=5, bg="#ffffff", bd=2, relief=tk.FLAT
    )
    self.lista_historial.pack(fill=tk.X, padx=15, pady=5)

  def clic_boton(self, valor):
    if valor == "C":
      self.pantalla_var.set("")
    elif valor == "=":
      try:
        expresion = self.pantalla_var.get()
        resultado = str(eval(expresion))
        self.pantalla_var.set(resultado)

        # Actualizar historial
        self.historial.append(f"{expresion} = {resultado}")
        if len(self.historial) > 5:
          self.historial.pop(0)  # Mantener solo las últimas 5

        self.actualizar_vista_historial()
      except Exception:
        self.pantalla_var.set("Error")
    else:
      actual = self.pantalla_var.get()
      self.pantalla_var.set(actual + valor)

  def actualizar_vista_historial(self):
    self.lista_historial.delete(0, tk.END)
    for op in reversed(self.historial):
      self.lista_historial.insert(tk.END, op)


if __name__ == "__main__":
  root = tk.Tk()
  app = CalculadoraTkinter(root)
  root.mainloop()