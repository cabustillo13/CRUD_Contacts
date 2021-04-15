# -*- coding: utf-8 -*-

"""Este módulo proporciona vistas para administrar la tabla Contactos."""

from PyQt5.QtWidgets import (
    QAbstractItemView,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)


class Window(QMainWindow):
    """Ventana principal."""

    def __init__(self, parent=None):
        """Inicializador."""
        super().__init__(parent)
        self.setWindowTitle("Lista de Contactos")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.setupUI()

    def setupUI(self):
        """Setup la GUI de la ventana principal."""
        # Crear la table view widget
        self.table = QTableView()
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        # Create buttons
        self.addButton = QPushButton("Añadir...")
        self.deleteButton = QPushButton("Borrar")
        self.clearAllButton = QPushButton("Borrar Todo")
        # Extender la GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)
