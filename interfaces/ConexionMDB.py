import mysql.connector

def conectar_a_MariaDB():
    try:
        # Reemplaza los valores de usuario, contraseña, host y nombre de la base de datos con los correctos
        connection = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='bank_karmant'
        )
        return connection
    except mysql.connector.Error as error:
        raise Exception(f"Error de conexión a MariaDB: {str(error)}")