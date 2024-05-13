from tkinter import Toplevel

import mysql

class ConexionMDB():
    def __init__(self, parent):
        try:
            connection = mysql.connector.connect(
                user='admin',
                password='12345',
                host='localhost',
                database='mundial_alemania_2006'
            )
            return connection
        except mysql.connector.Error as error:
            raise Exception(f"Error de conexión a MariaDB: {str(error)}")
