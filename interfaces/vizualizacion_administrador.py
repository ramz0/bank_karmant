from tkinter import Toplevel, ttk, messagebox
from customtkinter import CTkButton, CTkEntry
from ConexionMDB import conectar_a_MariaDB


class Interfaz_visualizacion_administrador(Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title("Interfaz Visualizacion Administrador")
        self.minsize(width=800, height=450)
        self.configure(bg="#2B8C57")

        # Frame para los campos
        frame_campos = ttk.Frame(self)
        frame_campos.pack(pady=20)

        # Recuadro de búsqueda
        self.entry_busqueda = CTkEntry(frame_campos)
        self.entry_busqueda.grid(row=0, column=0, padx=5)


        # Botón de visualización
        btn_visualizar_todos_los_retiros = CTkButton(frame_campos, text="Visualizar Todos los Retiros",
                                                     command=self.visualizar_t_retiros)
        btn_visualizar_todos_los_retiros.grid(row=0, column=2, padx=5)
        btn_visualizar_todas_las_transferencias = CTkButton(frame_campos, text="Visualizar Todos los Transacciones",
                                                            command=self.visualizar_t_transacciones)
        btn_visualizar_todas_las_transferencias.grid(row=0, column=3, padx=5)
        btn_visualizar_todos_los_depositos = CTkButton(frame_campos, text="Visualizar Todos los Depositos",
                                                       command=self.visualizar_t_depositos)
        btn_visualizar_todos_los_depositos.grid(row=0, column=4, padx=5)

        self.tree_depositos = ttk.Treeview(self, columns=('ID_CLIENTE_DEPOSITO', 'FECHA_DEPOSITO', 'MONTO_DEPOSITO'),
                                           show='headings')
        self.tree_depositos.column('ID_CLIENTE_DEPOSITO', width=100, anchor='center')
        self.tree_depositos.column('FECHA_DEPOSITO', width=150, anchor='center')
        self.tree_depositos.column('MONTO_DEPOSITO', width=200, anchor='center')

        self.tree_depositos.heading('ID_CLIENTE_DEPOSITO', text='ID_CLIENTE_DEPOSITO')
        self.tree_depositos.heading('FECHA_DEPOSITO', text='FECHA_DEPOSITO')
        self.tree_depositos.heading('MONTO_DEPOSITO', text='MONTO_DEPOSITO')
        self.tree_depositos.pack(pady=20)

        self.tree_retiros = ttk.Treeview(self, columns=('id_cliente_retira', 'fecha_hora_retiro', 'monto_de_retiro'),
                                         show='headings')
        self.tree_retiros.column('id_cliente_retira', width=100, anchor='center')
        self.tree_retiros.column('fecha_hora_retiro', width=150, anchor='center')
        self.tree_retiros.column('monto_de_retiro', width=200, anchor='center')

        self.tree_retiros.heading('id_cliente_retira', text='id_cliente_retira')
        self.tree_retiros.heading('fecha_hora_retiro', text='fecha_hora_retiro')
        self.tree_retiros.heading('monto_de_retiro', text='monto_de_retiro')
        self.tree_retiros.pack(pady=20)

        self.tree_transacciones = ttk.Treeview(self, columns=(
        'id_cliente_tranfiere', 'id_cliente_recibe', 'fecha_hora_transferencia', 'monto_de_tranferencia'),
                                               show='headings')
        self.tree_transacciones.column('id_cliente_tranfiere', width=100, anchor='center')
        self.tree_transacciones.column('id_cliente_recibe', width=150, anchor='center')
        self.tree_transacciones.column('fecha_hora_transferencia', width=200, anchor='center')
        self.tree_transacciones.column('monto_de_tranferencia', width=250, anchor='center')

        self.tree_transacciones.heading('id_cliente_tranfiere', text='id_cliente_tranfiere')
        self.tree_transacciones.heading('id_cliente_recibe', text='id_cliente_recibe')
        self.tree_transacciones.heading('fecha_hora_transferencia', text='fecha_hora_transferencia')
        self.tree_transacciones.heading('monto_de_tranferencia', text='monto_de_tranferencia')
        self.tree_transacciones.pack(pady=20)

        # Botón para regresar al menú principal
        btn_regresar = CTkButton(self, text="Regresar al Menú", command=self.regresar_a_menu)
        btn_regresar.pack(pady=10)

    def regresar_a_menu(self):
        self.destroy()

    def visualizar_t_retiros(self):
        try:
            conexion = conectar_a_MariaDB()
            cursor = conexion.cursor()

            consulta = "SELECT * FROM registro_retiro"

            cursor.execute(consulta)
            filas_rutas = cursor.fetchall()

            for item in self.tree_retiros.get_children():
                self.tree_retiros.delete(item)

            for fila in filas_rutas:
                self.tree_retiros.insert('', 'end', values=fila)

            cursor.close()
            conexion.close()

        except Exception as e:
            messagebox.showerror("Error", f"Error al visualizar los retiros: {str(e)}")

    def visualizar_t_transacciones(self):
        try:
            conexion = conectar_a_MariaDB()
            cursor = conexion.cursor()

            consulta = "SELECT * FROM registro_transferencia"

            cursor.execute(consulta)
            filas_transacciones = cursor.fetchall()

            for item in self.tree_transacciones.get_children():
                self.tree_transacciones.delete(item)

            for fila in filas_transacciones:
                self.tree_transacciones.insert('', 'end', values=fila)

            cursor.close()
            conexion.close()

        except Exception as e:
            messagebox.showerror("Error", f"Error al visualizar las transacciones: {str(e)}")

    def visualizar_t_depositos(self):
        try:
            conexion = conectar_a_MariaDB()
            cursor = conexion.cursor()

            consulta = "SELECT * FROM REGISTRO_DEPOSITO"

            cursor.execute(consulta)
            filas_depositos = cursor.fetchall()

            for item in self.tree_depositos.get_children():
                self.tree_depositos.delete(item)

            for fila in filas_depositos:
                self.tree_depositos.insert('', 'end', values=fila)

            cursor.close()
            conexion.close()

        except Exception as e:
            messagebox.showerror("Error", f"Error al visualizar los depositos: {str(e)}")


if __name__ == "__main__":
    interfaz_visualizar_administrador = Interfaz_visualizacion_administrador()
    interfaz_visualizar_administrador.mainloop()
