import sys
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class CalculadoraPySide6SinMenu(QWidget):

  def __init__(self):
    super().__init__()
    self.historial = []
    self.initUI()

  def initUI(self):
    self.setWindowTitle("Calculadora - PySide6 (Con Borrar e Historial)")
    self.setFixedSize(300, 580)

    main_layout = QVBoxLayout()

    # Pantalla (Modificado: se agregó "color: black;" para que los números se noten bien)
    self.pantalla = QLineEdit()
    self.pantalla.setFixedHeight(45)
    self.pantalla.setStyleSheet(
        "font-size: 20px; font-weight: bold; background-color: #f0f0f0; color:"
        " black;"
    )
    self.pantalla.setReadOnly(True)
    main_layout.addWidget(self.pantalla)

    # Botón de Borrar / Limpiar pantalla dedicado arriba de la botonera
    self.btn_limpiar = QPushButton("C (Limpiar Pantalla)")
    self.btn_limpiar.setFixedHeight(35)
    self.btn_limpiar.setStyleSheet(
        "font-size: 14px; font-weight: bold; background-color: #e74c3c; color:"
        " white;"
    )
    self.btn_limpiar.clicked.connect(self.limpiar_pantalla)
    main_layout.addWidget(self.btn_limpiar)

    # Botonera numérica y de operaciones
    grid_layout = QGridLayout()
    botones = [
        ("7", 0, 0),
        ("8", 0, 1),
        ("9", 0, 2),
        ("/", 0, 3),
        ("4", 1, 0),
        ("5", 1, 1),
        ("6", 1, 2),
        ("*", 1, 3),
        ("1", 2, 0),
        ("2", 2, 1),
        ("3", 2, 2),
        ("-", 2, 3),
        ("0", 3, 0),
        (".", 3, 1),
        ("=", 3, 2),
        ("+", 3, 3),
    ]

    for texto, fila, col in botones:
      btn = QPushButton(texto)
      btn.setFixedHeight(45)
      btn.setStyleSheet("font-size: 16px; font-weight: bold;")
      if texto == "=":
        btn.clicked.connect(self.calcular)
      else:
        btn.clicked.connect(
            lambda checked, t=texto: self.agregar_texto(t)
        )
      grid_layout.addWidget(btn, fila, col)

    main_layout.addLayout(grid_layout)

    # Historial (Últimas 5 operaciones)
    main_layout.addWidget(QPushButton("Historial (Últimas 5):"))
    self.lista_historial = QListWidget()
    self.lista_historial.setFixedHeight(110)
    main_layout.addWidget(self.lista_historial)

    self.setLayout(main_layout)

  def agregar_texto(self, texto):
    self.pantalla.setText(self.pantalla.text() + texto)

  def limpiar_pantalla(self):
    self.pantalla.clear()

  def calcular(self):
    expresion = self.pantalla.text()
    try:
      resultado = str(eval(expresion))
      self.pantalla.setText(resultado)

      # Actualizar historial
      self.historial.append(f"{expresion} = {resultado}")
      if len(self.historial) > 5:
        self.historial.pop(0)  # Mantener solo las últimas 5

      self.actualizar_vista_historial()
    except Exception:
      self.pantalla.setText("Error")

  def actualizar_vista_historial(self):
    self.lista_historial.clear()
    for op in reversed(self.historial):
      self.lista_historial.addItem(op)


if __name__ == "__main__":
  app = QApplication(sys.argv)
  calc = CalculadoraPySide6SinMenu()
  calc.show()
  sys.exit(app.exec())