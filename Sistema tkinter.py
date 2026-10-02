import tkinter as tk
from tkinter import messagebox, ttk


def registrar_usuario():
  nombre = entry_nombre.get()
  email = entry_email.get()
  pais = combo_pais.get()
  genero = genero_var.get()

  if not nombre or not email:
    messagebox.showerror(
        "Error", "Por favor completa los campos de nombre y correo."
    )
    return

  if terminos_var.get() == 0:
    messagebox.showwarning(
        "Advertencia", "Debes aceptar los términos y condiciones."
    )
    return

  messagebox.showinfo(
      "Éxito",
      f"Usuario registrado:\nNombre: {nombre}\nCorreo: {email}\nPaís:"
      f" {pais}\nGénero: {genero}",
  )


root = tk.Tk()
root.title("Sistema de Registro - Tkinter")
root.geometry("420x500")
root.resizable(False, False)

# Configuración de colores corporativos modernos
COLOR_BG = "#f8fafc"
COLOR_CARD = "#ffffff"
COLOR_PRIMARY = "#2563eb"
COLOR_HOVER = "#1d4ed8"
COLOR_TEXT = "#1e293b"
COLOR_MUTED = "#64748b"

root.configure(bg=COLOR_BG)

# Contenedor principal estilo Tarjeta (Card)
card_frame = tk.Frame(root, bg=COLOR_CARD, bd=0, highlightthickness=1, highlightbackground="#e2e8f0")
card_frame.place(x=30, y=25, width=360, height=450)

# Título y Subtítulo dentro de la tarjeta
tk.Label(
    card_frame, text="Registro de Usuario", font=("Segoe UI", 18, "bold"), bg=COLOR_CARD, fg=COLOR_TEXT
).pack(pady=(25, 5))

tk.Label(
    card_frame, text="Completa el formulario para continuar", font=("Segoe UI", 10), bg=COLOR_CARD, fg=COLOR_MUTED
).pack(pady=(0, 20))

# Formulario (Contenedor interno)
frame = tk.Frame(card_frame, bg=COLOR_CARD)
frame.pack(padx=25, fill="x")

# Estilos de etiquetas y campos
label_font = ("Segoe UI", 10, "bold")
input_font = ("Segoe UI", 10)

tk.Label(frame, text="Nombre:", font=label_font, bg=COLOR_CARD, fg=COLOR_TEXT).grid(
    row=0, column=0, sticky="w", pady=8
)
entry_nombre = tk.Entry(frame, width=24, font=input_font, bd=1, relief="solid")
entry_nombre.grid(row=0, column=1, pady=8, ipadx=3, ipady=2)

tk.Label(frame, text="Correo:", font=label_font, bg=COLOR_CARD, fg=COLOR_TEXT).grid(
    row=1, column=0, sticky="w", pady=8
)
entry_email = tk.Entry(frame, width=24, font=input_font, bd=1, relief="solid")
entry_email.grid(row=1, column=1, pady=8, ipadx=3, ipady=2)

tk.Label(frame, text="Género:", font=label_font, bg=COLOR_CARD, fg=COLOR_TEXT).grid(
    row=2, column=0, sticky="w", pady=8
)

genero_var = tk.StringVar(value="Masculino")
radio_frame = tk.Frame(frame, bg=COLOR_CARD)
radio_frame.grid(row=2, column=1, sticky="w", pady=8)

tk.Radiobutton(
    radio_frame, text="Masculino", variable=genero_var, value="Masculino", font=input_font, bg=COLOR_CARD, activebackground=COLOR_CARD, selectcolor=COLOR_CARD
).pack(side="left", padx=(0, 15))
tk.Radiobutton(
    radio_frame, text="Femenino", variable=genero_var, value="Femenino", font=input_font, bg=COLOR_CARD, activebackground=COLOR_CARD, selectcolor=COLOR_CARD
).pack(side="left")

tk.Label(frame, text="País:", font=label_font, bg=COLOR_CARD, fg=COLOR_TEXT).grid(
    row=3, column=0, sticky="w", pady=8
)
combo_pais = ttk.Combobox(
    frame,
    values=["México", "España", "Argentina", "Colombia", "Chile"],
    width=22,
    state="readonly",
    font=input_font,
)
combo_pais.grid(row=3, column=1, pady=8, ipadx=2, ipady=2)
combo_pais.current(0)

# Checkbox de Términos
terminos_var = tk.IntVar()
tk.Checkbutton(
    card_frame, text="Acepto los términos y condiciones", variable=terminos_var, font=("Segoe UI", 9), bg=COLOR_CARD, activebackground=COLOR_CARD, selectcolor=COLOR_CARD, fg=COLOR_TEXT
).pack(pady=(15, 10))

# Botón Registrar Moderno (Efectos visuales limpios)
btn_registrar = tk.Button(
    card_frame,
    text="Registrarse",
    bg=COLOR_PRIMARY,
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=22,
    relief="flat",
    cursor="hand2",
    command=registrar_usuario,
)
btn_registrar.pack(pady=10, ipady=4)

# Efectos hover simples para el botón
btn_registrar.bind("<Enter>", lambda e: btn_registrar.config(bg=COLOR_HOVER))
btn_registrar.bind("<Leave>", lambda e: btn_registrar.config(bg=COLOR_PRIMARY))

root.mainloop()