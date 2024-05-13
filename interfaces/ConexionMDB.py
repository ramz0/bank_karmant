import mysql

class ConexionMDB():
    def __init__(self, parent):
        try:
            connection = mysql.connector.connect(
                user='root',
                password='',
                host='localhost',
                database='bank_karmant'
            )
            return connection
        except mysql.connector.Error as error:
            raise Exception(f"Error de conexión a MariaDB: {str(error)}")
