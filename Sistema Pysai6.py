import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QCheckBox,
    QRadioButton,
    QComboBox,
    QMessageBox,
    QFrame,
    QButtonGroup,
)


class SistemaRegistroQt(QWidget):

  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    # Configuración de la ventana principal
    self.setWindowTitle("Sistema de Registro - PyQt / PySide")
    self.setFixedSize(440, 520)
    
    # Aplicar un estilo global moderno tipo hoja de estilos (QSS)
    self.setStyleSheet("""
        QWidget {
            background-color: #f4f6f9;
            font-family: 'Segoe UI', Arial, sans-serif;
            color: #2c3e50;
        }
        QLineEdit {
            background-color: #ffffff;
            border: 1px solid #dcdde1;
            border-radius: 6px;
            padding: 8px 12px;
            font-size: 13px;
            selection-background-color: #3498db;
        }
        QLineEdit:focus {
            border: 2px solid #3498db;
        }
        QComboBox {
            background-color: #ffffff;
            border: 1px solid #dcdde1;
            border-radius: 6px;
            padding: 6px 12px;
            font-size: 13px;
        }
        QComboBox::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 25px;
            border-left-width: 0px;
        }
        QRadioButton {
            spacing: 8px;
            font-size: 13px;
            color: #34495e;
        }
        /* Cambio de color y estilo al seleccionar el RadioButton */
        QRadioButton:checked {
            color: #2563eb;
            font-weight: bold;
        }
        QCheckBox {
            spacing: 8px;
            font-size: 13px;
        }
        QLabel {
            font-size: 13px;
            color: #34495e;
        }
    """)

    # Layout principal (Vertical)
    main_layout = QVBoxLayout()
    main_layout.setContentsMargins(25, 25, 25, 25)
    main_layout.setSpacing(15)

    # Contenedor estilo Tarjeta (Card)
    card = QFrame()
    card.setStyleSheet("""
        QFrame {
            background-color: #ffffff;
            border-radius: 12px;
            border: 1px solid #e1e8ed;
        }
    """)
    card_layout = QVBoxLayout(card)
    card_layout.setContentsMargins(20, 20, 20, 20)
    card_layout.setSpacing(15)

    # Título elegante
    titulo = QLabel("Registro de Usuario")
    titulo.setStyleSheet("font-size: 20px; font-weight: bold; color: #1e293b;")
    card_layout.addWidget(titulo)

    # Subtítulo descriptivo
    subtitulo = QLabel("Complete sus datos para crear una cuenta")
    subtitulo.setStyleSheet("font-size: 12px; color: #64748b; margin-bottom: 5px;")
    card_layout.addWidget(subtitulo)

    # Layout de Formulario (para alinear etiquetas y entradas)
    form_layout = QFormLayout()
    form_layout.setSpacing(12)
    form_layout.setLabelAlignment(Qt.AlignLeft)

    self.input_nombre = QLineEdit()
    self.input_nombre.setPlaceholderText("Ingresa tu nombre")
    form_layout.addRow(QLabel("Nombre:"), self.input_nombre)

    self.input_email = QLineEdit()
    self.input_email.setPlaceholderText("correo@ejemplo.com")
    form_layout.addRow(QLabel("Correo:"), self.input_email)

    # Botones de opción (Radio Buttons) para género agrupados correctamente
    self.radio_masculino = QRadioButton("Masculino")
    self.radio_femenino = QRadioButton("Femenino")
    self.radio_masculino.setChecked(True)

    # Agrupador lógico para exclusión mutua
    self.grupo_genero = QButtonGroup(self)
    self.grupo_genero.addButton(self.radio_masculino)
    self.grupo_genero.addButton(self.radio_femenino)

    radio_layout = QHBoxLayout()
    radio_layout.addWidget(self.radio_masculino)
    radio_layout.addWidget(self.radio_femenino)
    radio_layout.addStretch()
    form_layout.addRow(QLabel("Género:"), radio_layout)

    # Selector desplegable (ComboBox) para país
    self.combo_pais = QComboBox()
    self.combo_pais.addItems(
        ["México", "España", "Argentina", "Colombia", "Chile"]
    )
    form_layout.addRow(QLabel("País:"), self.combo_pais)

    card_layout.addLayout(form_layout)

    # Casilla de verificación (CheckBox) para términos
    self.check_terminos = QCheckBox("Acepto los términos y condiciones")
    card_layout.addWidget(self.check_terminos)

    # Botón de envío (QPushButton) con diseño moderno y efecto hover
    self.btn_registrar = QPushButton("Registrarse")
    self.btn_registrar.setFixedHeight(42)
    self.btn_registrar.setStyleSheet("""
        QPushButton {
            background-color: #2563eb;
            color: white;
            font-weight: bold;
            font-size: 14px;
            border-radius: 6px;
            border: none;
        }
        QPushButton:hover {
            background-color: #1d4ed8;
        }
        QPushButton:pressed {
            background-color: #1e40af;
        }
    """)
    self.btn_registrar.clicked.connect(self.procesar_registro)
    card_layout.addWidget(self.btn_registrar)

    main_layout.addWidget(card)
    self.setLayout(main_layout)

  def procesar_registro(self):
    nombre = self.input_nombre.text()
    email = self.input_email.text()
    pais = self.combo_pais.currentText()
    
    # Obtener el texto del botón de radio seleccionado mediante el grupo
    genero_activo = self.grupo_genero.checkedButton()
    genero = genero_activo.text() if genero_activo else "No especificado"

    # Validaciones básicas
    if not nombre or not email:
      QMessageBox.warning(
          self,
          "Campos Vacíos",
          "Por favor completa el nombre y el correo electrónico.",
      )
      return

    if not self.check_terminos.isChecked():
      QMessageBox.warning(
          self,
          "Términos Requeridos",
          "Debes aceptar los términos y condiciones para continuar.",
      )
      return

    # Mensaje de éxito
    QMessageBox.information(
        self,
        "¡Registro Exitoso!",
        f"Bienvenido/a, {nombre}.\nCorreo: {email}\nGénero: {genero}\nPaís: {pais}",
    )


if __name__ == "__main__":
  app = QApplication(sys.argv)
  ventana = SistemaRegistroQt()
  ventana.show()
  sys.exit(app.exec())