# -*- coding: utf-8 -*-

"""Este módulo proporciona una conexión de base de datos.."""

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def _createContactsTable():
    """Crea la tabla de contactos en la base de datos.."""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(40) NOT NULL,
            job VARCHAR(50),
            email VARCHAR(40) NOT NULL
        )
        """
    )


def createConnection(databaseName):
    """Crea y abre una conexión de base de datos.."""
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            None,
            "Database de Contactos 2021",
            f"Database Error: {connection.lastError().text()}",
        )
        return False

    _createContactsTable()
    return True 
