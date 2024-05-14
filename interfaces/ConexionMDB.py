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
        print('Conexion Exitosa')
        return connection
    except mysql.connector.Error as error:
        raise Exception(f"Error de conexión a MariaDB: {str(error)}")


# Operaciones CRUD.
def ejecutar_consulta(query, parametros=None):
    try:
        connection = conectar_a_MariaDB()
        cursor = connection.cursor()
        if parametros:
            cursor.execute(query, parametros)
        else:
            print(query)
            cursor.execute(query)
        result = cursor.fetchall()  # Leer todos los resultados antes de cerrar el cursor
        connection.commit()
        return result
    except mysql.connector.Error as error:
        raise Exception(f"Error al ejecutar consulta: {str(error)}")
    finally:
        cursor.close()
        connection.close()



def select(tabla, condiciones=None):
    query = f"SELECT * FROM {tabla}"
    if condiciones:
        query += f" WHERE {condiciones}"
    return ejecutar_consulta(query)


def insert(tabla, valores):
    try:
        connection = conectar_a_MariaDB()
        cursor = connection.cursor()
        placeholders = ', '.join(['%s'] * len(valores))
        query = f"INSERT INTO {tabla} VALUES ({placeholders})"
        cursor.execute(query, valores)  # Pasar directamente el array de valores
        connection.commit()
        print("Registro insertado correctamente.")
    except mysql.connector.Error as error:
        raise Exception(f"Error al insertar registro: {str(error)}")
    finally:
        cursor.close()
        connection.close()




def update(tabla, valores, condiciones):
    try:
        connection = conectar_a_MariaDB()
        cursor = connection.cursor()
        
        # Convertir la lista de valores en una cadena de cambios
        cambios = ', '.join([f"{campo} = %s" for campo in valores[::2]])
        
        # Obtener los valores a actualizar
        valores_a_actualizar = valores[1::2]
        
        # Construir la consulta SQL
        query = f"UPDATE {tabla} SET {cambios} WHERE {condiciones}"
        
        # Ejecutar la consulta con los valores correspondientes
        cursor.execute(query, valores_a_actualizar)
        
        connection.commit()
        print("Registros actualizados correctamente.")
    except mysql.connector.Error as error:
        raise Exception(f"Error al actualizar registros: {str(error)}")
    finally:
        cursor.close()
        connection.close()



def delete(tabla, condiciones):
    try:
        connection = conectar_a_MariaDB()
        cursor = connection.cursor()
        
        # Construir la consulta SQL
        query = f"DELETE FROM {tabla} WHERE {condiciones}"
        
        # Ejecutar la consulta
        cursor.execute(query)
        
        connection.commit()
        print("Registros eliminados correctamente.")
    except mysql.connector.Error as error:
        raise Exception(f"Error al eliminar registros: {str(error)}")
    finally:
        cursor.close()
        connection.close()




# Ejemplos de uso:

# Seleccionar todos los registros de la tabla 'usuarios'
# resultado = select('cuenta')
# for registro in resultado:
#     print(registro)

# Insertar un nuevo usuario
# nuevoTipoCuenta = ['6', 'TARJETA VERD3']
# insert('tipo_cuenta', nuevoTipoCuenta)

# Actualizar el nombre del usuario con ID 1
# update('tipo_cuenta', ['TIPO_CUENTA', 'TARJETA VERDE'], 'ID_TIPO_CUENTA = 6')

# Eliminar usuarios con nombre 'Juan'
# delete('tipo_cuenta', "id_tipo_cuenta = 6")