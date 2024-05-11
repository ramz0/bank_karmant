from PIL import Image
import customtkinter as ctk

class DashboardMenuCliente(ctk.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Cargar la imagen de fondo
        self.configure(fg_color='#45475a')

        # Cargar la imagen del logo con fondo transparente
        self.img_logo_banco = ctk.CTkImage(light_image=Image.open('assets/icono_banco.png'), size=(200,200))
        
        # Crear el CTkLabel para el logo
        self.lbl_logo_banco = ctk.CTkLabel(self, image=self.img_logo_banco, anchor='center', text='', fg_color='transparent')
        self.lbl_logo_banco.grid(row=0, column=0, pady=5, padx=20)

        # Crear el nombre del banco
        self.nombre_banco = ctk.CTkLabel(self, text="BANK KARMNAT", text_color='#11111b', anchor='center', font=('Roboto', 24))
        self.nombre_banco.grid(row=1, column=0, padx=10, columnspan=2)

        # Espacio
        self.espacio_1 = ctk.CTkFrame(self, width=1, height=30)
        self.espacio_1.grid(row=2, column=0)

        # Botones del menú
        self.nombre_botones_menu = ['DEPOSITO', 'TRANSFERENCIA', 'RETIRO']
        self.orden_botones = 3
        for str_btn in self.nombre_botones_menu:
            btn_deposito = ctk.CTkButton(self, text=str_btn, fg_color='#89b4fa', corner_radius=5, height=40, anchor='center', text_color='#45475a')
            btn_deposito.grid(row=self.orden_botones, column=0, pady=5, columnspan=2)
            self.orden_botones += 1

        # Espacio 2
        self.espacio_2 = ctk.CTkFrame(self, width=1, height=180)
        self.espacio_2.grid(row=self.orden_botones, column=0)

        self.orden_botones += 1

        # Botón para cerrar sesión
        self.btn_cerrar_sesion = ctk.CTkButton(self, text='CERRAR SESIÓN', fg_color='#45475a', text_color='white', anchor='center')
        self.btn_cerrar_sesion.grid(row=self.orden_botones, column=0, pady=5)

        # Diseño auto ajustable
        self.rowconfigure(0, weight=1)
        self.nombre_banco.columnconfigure(0, weight=1)
