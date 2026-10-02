import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class Calculadora4PySide6(QMainWindow):

  def __init__(self):
    super().__init__()
    self.historial = []
    self.initUI()

  def initUI(self):
    self.setWindowTitle("Calculadora 4 - PySide6 (Pro con Menú)")
    self.setFixedSize(320, 600)

    # Menú Superior Avanzado
    menu_bar = self.menuBar()

    menu_edicion = menu_bar.addMenu("Edición")
    accion_borrar = QAction("Borrar pantalla", self)
    accion_borrar.triggered.connect(lambda: self.pantalla.clear())
    menu_edicion.addAction(accion_borrar)

    menu_opciones = menu_bar.addMenu("Temas")
    accion_oscuro = QAction("Modo Oscuro", self)
    accion_oscuro.triggered.connect(self.tema_oscuro)
    menu_opciones.addAction(accion_oscuro)

    accion_claro = QAction("Modo Claro", self)
    accion_claro.triggered.connect(self.tema_claro)
    menu_opciones.addAction(accion_claro)

    menu_ayuda = menu_bar.addMenu("Ayuda")
    accion_info = QAction("Acerca de...", self)
    accion_info.triggered.connect(
        lambda: QMessageBox.information(
            self,
            "Acerca de",
            "Calculadora 4 - PySide6\nCon menú y registro de historial.",
        )
    )
    menu_ayuda.addAction(accion_info)

    central_widget = QWidget()
    main_layout = QVBoxLayout()

    # Pantalla de la calculadora
    self.pantalla = QLineEdit()
    self.pantalla.setFixedHeight(45)
    self.pantalla.setStyleSheet(
        "font-size: 22px; font-weight: bold; background-color: #ffffff;"
        " color: #000000; border: 2px solid #ccc; border-radius: 5px;"
    )
    self.pantalla.setReadOnly(True)
    main_layout.addWidget(self.pantalla)

    # Botón de Borrar / Limpiar ('C') dedicado
    self.btn_limpiar = QPushButton("C (Limpiar Pantalla)")
    self.btn_limpiar.setFixedHeight(35)
    self.btn_limpiar.setStyleSheet(
        "font-size: 14px; font-weight: bold; background-color: #e74c3c; color:"
        " white;"
    )
    self.btn_limpiar.clicked.connect(lambda: self.pantalla.clear())
    main_layout.addWidget(self.btn_limpiar)

    # Botonera (Grid)
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

    self.botones_lista = []
    for texto, fila, col in botones:
      btn = QPushButton(texto)
      btn.setFixedHeight(45)
      btn.setStyleSheet(
          "font-size: 16px; font-weight: bold; background-color: #f9f9f9;"
          " color: #000000;"
      )
      if texto == "=":
        btn.clicked.connect(self.calcular)
      else:
        btn.clicked.connect(
            lambda checked, t=texto: self.agregar_texto(t)
        )
      grid_layout.addWidget(btn, fila, col)
      self.botones_lista.append(btn)

    main_layout.addLayout(grid_layout)

    # Historial (Últimas 5 operaciones)
    self.label_historial = QPushButton("Historial (Últimas 5):")
    main_layout.addWidget(self.label_historial)
    self.lista_historial = QListWidget()
    self.lista_historial.setFixedHeight(110)
    main_layout.addWidget(self.lista_historial)

    central_widget.setLayout(main_layout)
    self.setCentralWidget(central_widget)

  def agregar_texto(self, texto):
    self.pantalla.setText(self.pantalla.text() + texto)

  def calcular(self):
    expresion = self.pantalla.text()
    try:
      resultado = str(eval(expresion))
      self.pantalla.setText(resultado)

      # Actualizar historial (últimas 5)
      self.historial.append(f"{expresion} = {resultado}")
      if len(self.historial) > 5:
        self.historial.pop(0)

      self.actualizar_historial()
    except Exception:
      self.pantalla.setText("Error")

  def actualizar_historial(self):
    self.lista_historial.clear()
    for op in reversed(self.historial):
      self.lista_historial.addItem(op)

  def tema_oscuro(self):
    # Fondo general más oscuro
    self.setStyleSheet("background-color: #181818; color: #e0e0e0;")
    
    # Pantalla con tonos oscuros y texto claro pero no deslumbrante
    self.pantalla.setStyleSheet(
        "font-size: 22px; font-weight: bold; background-color: #242424; color:"
        " #ffffff; border: 2px solid #444;"
    )
    
    # Ajustar botones de la calculadora a un gris más oscuro y texto visible
    for btn in self.botones_lista:
      btn.setStyleSheet(
          "font-size: 16px; font-weight: bold; background-color: #2c2c2c;"
          " color: #e0e0e0; border: 1px solid #3a3a3a;"
      )
      
    # Ajustar historial y su etiqueta
    self.label_historial.setStyleSheet("background-color: #2c2c2c; color: #e0e0e0;")
    self.lista_historial.setStyleSheet(
        "background-color: #202020; color: #e0e0e0; border: 1px solid #444;"
    )

  def tema_claro(self):
    self.setStyleSheet("")
    self.pantalla.setStyleSheet(
        "font-size: 22px; font-weight: bold; background-color: #ffffff; color:"
        " #000000; border: 2px solid #ccc;"
    )
    for btn in self.botones_lista:
      btn.setStyleSheet(
          "font-size: 16px; font-weight: bold; background-color: #f9f9f9;"
          " color: #000000;"
      )
    self.label_historial.setStyleSheet("")
    self.lista_historial.setStyleSheet("")


if __name__ == "__main__":
  app = QApplication(sys.argv)
  calc = Calculadora4PySide6()
  calc.show()
  sys.exit(app.exec())