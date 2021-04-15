# -*- coding: utf-8 -*-

"""Este módulo proporciona la aplicación Contactos."""

import sys

from PyQt5.QtWidgets import QApplication

from .views import Window


def main():
    """Contactos -> Función principal."""
    # Crear la aplicación
    app = QApplication(sys.argv)
    # Crear la ventana principal
    win = Window()
    win.show()
    # Ejecutar en un loop este evento
    sys.exit(app.exec()) 
