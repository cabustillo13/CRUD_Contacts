# -*- coding: utf-8 -*-

"""Este módulo proporciona la aplicación Contactos."""

import sys

from PyQt5.QtWidgets import QApplication

from .database import createConnection
from .views import Window


def main():
    """Contactos -> Función principal."""
    # Crear la aplicación
    app = QApplication(sys.argv)
    # Conectar a la base de datos antes de crear cualquier ventana
    if not createConnection("contacts.sqlite"):
        sys.exit(1)
    # Crear la ventana principa si la conexión fue exitosa
    win = Window()
    win.show()
    # Ejecutar en un loop este evento
    sys.exit(app.exec_())
