import customtkinter as ctk
from tkinter import messagebox

# Configuración inicial de apariencia
ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")


def registrar_usuario():
  nombre = entry_nombre.get()
  email = entry_email.get()
  pais = combo_pais.get()

  if not nombre or not email:
    messagebox.showerror("Error", "Rellene todos los campos obligatorios.")
    return

  messagebox.showinfo(
      "Éxito", f"¡Bienvenido, {nombre}! Registro completado con éxito."
  )


app = ctk.CTk()
app.title("Sistema de Registro - CustomTkinter")
app.geometry("400x500")
app.resizable(False, False)

# Título
label_titulo = ctk.CTkLabel(
    app, text="Registro Moderno", font=ctk.CTkFont(size=20, weight="bold")
)
label_titulo.pack(pady=20)

# Entradas y Controles
entry_nombre = ctk.CTkEntry(
    app, placeholder_text="Nombre completo", width=300, height=35
)
entry_nombre.pack(pady=10)

entry_email = ctk.CTkEntry(
    app, placeholder_text="Correo electrónico", width=300, height=35
)
entry_email.pack(pady=10)

combo_pais = ctk.CTkComboBox(
    app,
    values=["México", "España", "Argentina", "Colombia", "Chile"],
    width=300,
    height=35,
)
combo_pais.pack(pady=10)
combo_pais.set("Seleccione su país")

check_terminos = ctk.CTkCheckBox(
    app, text="Acepto términos y condiciones", font=ctk.CTkFont(size=12)
)
check_terminos.pack(pady=15, padx=50, anchor="w")

btn_registrar = ctk.CTkButton(
    app,
    text="Registrarse",
    command=registrar_usuario,
    width=200,
    height=40,
    font=ctk.CTkFont(size=14, weight="bold"),
)
btn_registrar.pack(pady=20)

app.mainloop()