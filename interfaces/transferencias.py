from tkinter import Toplevel, ttk, messagebox
from customtkinter import CTkButton, CTkEntry
from ConexionMDB import conectar_a_MariaDB
import decimal
from tkinter import Button

class Interfaz_transferencias(Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title("Interfaz Transferencias")
        self.minsize(width=500, height=550)
        self.configure(bg="#2B8C57")

        self.conexion_db = conectar_a_MariaDB()
        self.cursor_db = self.conexion_db.cursor()

        frame_campos = ttk.Frame(self)
        frame_campos.pack(pady=20)

        ttk.Label(frame_campos, text="Cuenta Origen:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_cuenta_origen = CTkEntry(frame_campos)
        self.entry_cuenta_origen.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_campos, text="Cuenta Destino:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_cuenta_destino = CTkEntry(frame_campos)
        self.entry_cuenta_destino.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_campos, text="Monto:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_monto = CTkEntry(frame_campos)
        self.entry_monto.grid(row=2, column=1, padx=5, pady=5)

        self.btn_transferir = CTkButton(frame_campos, text="Transferir", command=self.transferir)
        self.btn_transferir.grid(row=3, columnspan=2, pady=10)

        # Botón para regresar al menú principal
        self.btn_regresar = Button(frame_campos, text="Regresar al Menú", command=self.regresar_menu)
        self.btn_regresar.grid(row=4, columnspan=2, pady=10)

    def obtener_saldo_cuenta(self, numero_cuenta):
        query = f"SELECT SALDO FROM CUENTA WHERE NUMERO_CUENTA = '{numero_cuenta}'"
        self.cursor_db.execute(query)
        saldo = self.cursor_db.fetchone()
        if saldo:
            return saldo[0]
        else:
            return None

    def actualizar_saldo_cuenta(self, numero_cuenta, nuevo_saldo):
        query = f"UPDATE CUENTA SET SALDO = {nuevo_saldo} WHERE NUMERO_CUENTA = '{numero_cuenta}'"
        self.cursor_db.execute(query)
        self.conexion_db.commit()

    def transferir(self):
        cuenta_origen = self.entry_cuenta_origen.get()
        cuenta_destino = self.entry_cuenta_destino.get()
        monto = self.entry_monto.get()

        # Verificar si los campos están vacíos
        if not cuenta_origen or not cuenta_destino or not monto:
            messagebox.showerror("Campos vacíos", "Por favor complete todos los campos.")
            return  # Salir del método si hay campos vacíos

        # Convertir monto a Decimal
        monto = decimal.Decimal(monto)

        saldo_origen = self.obtener_saldo_cuenta(cuenta_origen)
        saldo_destino = self.obtener_saldo_cuenta(cuenta_destino)

        if saldo_origen is not None and saldo_origen >= monto:
            nuevo_saldo_origen = saldo_origen - monto
            nuevo_saldo_destino = saldo_destino + monto  # Sumar el monto al saldo de destino
            self.actualizar_saldo_cuenta(cuenta_origen, nuevo_saldo_origen)
            self.actualizar_saldo_cuenta(cuenta_destino, nuevo_saldo_destino)
            messagebox.showinfo("Transferencia exitosa",
                                f"Transferencia de ${monto} realizada de {cuenta_origen} a {cuenta_destino}")
            self.entry_cuenta_origen.delete(0, 'end')  # Limpiar el campo de cuenta origen
            self.entry_cuenta_destino.delete(0, 'end')  # Limpiar el campo de cuenta destino
            self.entry_monto.delete(0, 'end')  # Limpiar el campo de monto
        else:
            messagebox.showerror("Error de saldo", "Saldo insuficiente en la cuenta de origen")

        self.conexion_db.close()

    def regresar_menu(self):
        self.destroy()

if __name__ == "__main__":
    interfaz_transferencias = Interfaz_transferencias()
    interfaz_transferencias.mainloop()
