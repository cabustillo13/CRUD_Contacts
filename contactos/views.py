# -*- coding: utf-8 -*-

"""This module provides views to manage the contacts table."""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)

from .model import ContactsModel


class Window(QMainWindow):
    """Ventana Principal."""

    def __init__(self, parent=None):
        """Inicializador."""
        super().__init__(parent)
        self.setWindowTitle("Database de Contactos 2021")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.contactsModel = ContactsModel()
        self.setupUI()

    def setupUI(self):
        """Setup la GUI de la ventana principal."""
        # Crear la table view widget
        self.table = QTableView()
        self.table.setModel(self.contactsModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        # Crear botones
        self.addButton = QPushButton("Añadir...")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Borrar")
        self.deleteButton.clicked.connect(self.deleteContact)
        self.clearAllButton = QPushButton("Borrar Todo")
        self.clearAllButton.clicked.connect(self.clearContacts)
        # Extender la GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

    def openAddDialog(self):
        """Abrir el cuadro de dialogo de "Agregar contacto"."""
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.contactsModel.addContact(dialog.data)
            self.table.resizeColumnsToContents()

    def deleteContact(self):
        """Eliminar el contacto seleccionado de la base de datos."""
        row = self.table.currentIndex().row()
        if row < 0:
            return

        messageBox = QMessageBox.warning(
            self,
            "¡Cuidado!",
            "¿Deseas remover el contacto seleccionado?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.contactsModel.deleteContact(row)

    def clearContacts(self):
        """Remover todos los contactos de la base de datos."""
        messageBox = QMessageBox.warning(
            self,
            "¡Cuidado!",
            "¿Deseas remover todos los contactos seleccionados?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.contactsModel.clearContacts()


class AddDialog(QDialog):
    """Agregar el cuadro de diálogo de "Añadir contacto"."""

    def __init__(self, parent=None):
        """Inicializador."""
        super().__init__(parent=parent)
        self.setWindowTitle("Agregar Contacto")
        self.resize(250, 150)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()

    def setupUI(self):
        """Setup el cuadro de dialógo de "Añadir contacto"."""
        # Crear líneas editables para llenar los campos de datos.
        self.nameField = QLineEdit()
        self.nameField.setObjectName("Name")
        self.jobField = QLineEdit()
        self.jobField.setObjectName("Job")
        self.emailField = QLineEdit()
        self.emailField.setObjectName("Email")
        # Extender los campos de datos.
        layout = QFormLayout()
        layout.addRow("Nombre:", self.nameField)
        layout.addRow("Cargo:", self.jobField)
        layout.addRow("Email:", self.emailField)
        self.layout.addLayout(layout)
        # Agregar botones standards al cuadro de dialogo y conectarlos entre sí.
        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonsBox)

    def accept(self):
        """Aceptar la data que proviene de los cuadros de diálogo."""
        self.data = []
        for field in (self.nameField, self.jobField, self.emailField):
            if not field.text():
                QMessageBox.critical(
                    self,
                    "¡Error!",
                    f"Debes proveer un nombre de contacto {field.objectName()}",
                )
                self.data = None  # Resetear la data
                return

            self.data.append(field.text())

        if not self.data:
            return

        super().accept() 
