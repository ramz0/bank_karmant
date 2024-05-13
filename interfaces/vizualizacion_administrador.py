from tkinter import Toplevel, ttk, messagebox
from customtkinter import CTkButton, CTkEntry
from ConexionMDB import ConexionMDB

class Interfazconsultarutas(Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title("Interfaz de Consulta de Rutas")
        self.minsize(width=900, height=800)
        self.configure(bg="#f39c12")

        # Frame para los campos
        frame_campos = ttk.Frame(self)
        frame_campos.pack(pady=20)

        # Recuadro de búsqueda
        self.entry_busqueda = CTkEntry(frame_campos)
        self.entry_busqueda.grid(row=0, column=0, padx=5)

        # Botón de búsqueda
        btn_buscar = CTkButton(frame_campos, text="Buscar Ruta", command=self.buscar_ruta)  # Sin paréntesis
        btn_buscar.grid(row=0, column=1, padx=5)

        # Botón de visualización
        btn_visualizar = CTkButton(frame_campos, text="Visualizar Todas", command=self.visualizar_rutas)  # Sin paréntesis
        btn_visualizar.grid(row=0, column=2, padx=5)

        # Crear la tabla ttk.Treeview para mostrar los registros de estadios
        self.tree_rutas = ttk.Treeview(self, columns=('cod_ruta', 'origen', 'destino_final', 'km_recorridos'), show='headings')
        self.tree_rutas.column('cod_ruta', width=100, anchor='center')
        self.tree_rutas.column('origen', width=150, anchor='center')
        self.tree_rutas.column('destino_final', width=200, anchor='center')
        self.tree_rutas.column('km_recorridos', width=200, anchor='center')

        self.tree_rutas.heading('cod_ruta', text='cod_ruta')
        self.tree_rutas.heading('origen', text='origen')
        self.tree_rutas.heading('destino_final', text='destino_final')
        self.tree_rutas.heading('km_recorridos', text='km_recorridos')

        self.tree_rutas.pack(pady=20)

        # Botón para regresar al menú principal
        btn_regresar = CTkButton(self, text="Regresar al Menú", command=self.regresar_a_menu)
        btn_regresar.pack(pady=10)

    def regresar_a_menu(self):
        self.destroy()  # Cierra la interfaz de Estadios

    def visualizar_rutas(self):
        try:
            # Lógica para visualizar la información de estadios desde la base de datos
            conexion = ConexionMDB()
            cursor = conexion.cursor()

            consulta = "SELECT * FROM ruta"

            # Ejecutar la consulta
            cursor.execute(consulta)
            filas_rutas = cursor.fetchall()

            # Limpiar la tabla antes de cargar nuevos datos
            for item in self.tree_rutas.get_children():
                self.tree_rutas.delete(item)

            # Insertar las filas de estadios en la tabla ttk.Treeview
            for fila in filas_rutas:
                self.tree_rutas.insert('', 'end', values=fila)

            # Cerrar el cursor y la conexión
            cursor.close()
            conexion.close()

        except Exception as e:
            messagebox.showerror("Error", f"Error al visualizar las rutas: {str(e)}")

    def buscar_ruta(self):
        texto_busqueda = self.entry_busqueda.get()
        if texto_busqueda:
            try:
                # Lógica para buscar el estadio por nombre o ciudad desde la base de datos
                conexion = conectar_a_MariaDB()
                cursor = conexion.cursor()

                consulta = f"SELECT * FROM ruta WHERE COD_RUTA LIKE '%{texto_busqueda}%' OR ORIGEN LIKE '%{texto_busqueda}%'"

                # Ejecutar la consulta
                cursor.execute(consulta)
                filas_ruta = cursor.fetchall()

                # Limpiar la tabla antes de cargar nuevos datos
                for item in self.tree_rutas.get_children():
                    self.tree_rutas.delete(item)

                # Insertar las filas de estadios encontrados en la tabla ttk.Treeview
                for fila in filas_ruta:
                    self.tree_rutas.insert('', 'end', values=fila)

                # Cerrar el cursor y la conexión
                cursor.close()
                conexion.close()

            except Exception as e:
                messagebox.showerror("Error", f"Error al buscar la ruta: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "Ingresa el nombre de la ruta o ciudad para buscar.")


if __name__ == "__main__":
    interfaz_consultarutas = Interfazconsultarutas(None)
    interfaz_consultarutas.mainloop()
