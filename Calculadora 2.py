import wx


class CalculadoraWxPythonSinMenu(wx.Frame):

  def __init__(self):
    super().__init__(
        parent=None,
        title="Calculadora 2 - wxPython (Sin Menú)",
        size=(320, 540),
    )

    self.historial = []
    self.initUI()
    self.Centre()
    self.Show()

  def initUI(self):
    panel = wx.Panel(self)
    main_sizer = wx.BoxSizer(wx.VERTICAL)

    # 1. Pantalla de la calculadora
    self.pantalla = wx.TextCtrl(
        panel, style=wx.TE_RIGHT | wx.TE_READONLY, size=(-1, 45)
    )
    fuente_pantalla = wx.Font(
        18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD
    )
    self.pantalla.SetFont(fuente_pantalla)
    main_sizer.Add(self.pantalla, 0, wx.EXPAND | wx.ALL, 10)

    # 2. Botonera (Grid)
    grid_sizer = wx.GridSizer(rows=4, cols=4, hgap=5, vgap=5)

    botones = [
        "7",
        "8",
        "9",
        "/",
        "4",
        "5",
        "6",
        "*",
        "1",
        "2",
        "3",
        "-",
        "0",
        "C",
        "=",
        "+",
    ]

    for texto in botones:
      btn = wx.Button(panel, label=texto, size=(-1, 45))
      fuente_btn = wx.Font(
          14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD
      )
      btn.SetFont(fuente_btn)

      if texto == "C":
        btn.SetBackgroundColour(wx.Colour(231, 76, 60))  # Rojo para borrar
        btn.SetForegroundColour(wx.WHITE)
        btn.Bind(wx.EVT_BUTTON, self.on_borrar_pantalla)
      elif texto == "=":
        btn.SetBackgroundColour(wx.Colour(46, 204, 113))  # Verde para igual
        btn.SetForegroundColour(wx.WHITE)
        btn.Bind(wx.EVT_BUTTON, self.on_calcular)
      else:
        btn.Bind(
            wx.EVT_BUTTON,
            lambda event, t=texto: self.on_boton_presionado(event, t),
        )

      grid_sizer.Add(btn, 0, wx.EXPAND)

    main_sizer.Add(grid_sizer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

    # 3. Historial (Últimas 5 operaciones)
    lbl_historial = wx.StaticText(panel, label="Historial (Últimas 5):")
    main_sizer.Add(lbl_historial, 0, wx.LEFT | wx.TOP, 10)

    self.lista_historial = wx.ListBox(panel, size=(-1, 110))
    main_sizer.Add(
        self.lista_historial, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 10
    )

    panel.SetSizer(main_sizer)

  def on_boton_presionado(self, event, texto):
    texto_actual = self.pantalla.GetValue()
    self.pantalla.SetValue(texto_actual + texto)

  def on_borrar_pantalla(self, event):
    self.pantalla.Clear()

  def on_calcular(self, event):
    expresion = self.pantalla.GetValue()
    try:
      resultado = str(eval(expresion))
      self.pantalla.SetValue(resultado)

      # Actualizar historial (últimas 5)
      self.historial.append(f"{expresion} = {resultado}")
      if len(self.historial) > 5:
        self.historial.pop(0)

      self.actualizar_vista_historial()
    except Exception:
      self.pantalla.SetValue("Error")

  def actualizar_vista_historial(self):
    self.lista_historial.Clear()
    for op in reversed(self.historial):
      self.lista_historial.Append(op)


if __name__ == "__main__":
  app = wx.App(False)
  frame = CalculadoraWxPythonSinMenu()
  app.MainLoop()