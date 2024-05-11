from PIL import Image
import customtkinter as ctk

class DashboardMenuCliente(ctk.CTkFrame):
    colorMenu = '#2B8C57'
    direccionIconoBanco = 'assets/logobanco.png'
    # nombreBanco = "BANK KARMNAT"
    nombreBanco = ""
    txtCerrarSesion = 'CERRAR SESIÓN'
    
    seleccionBoton = '#FFFEFF'
    colorTextMenu = seleccionBoton

    def __init__(self, parent, button_names, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Cargar la imagen de fondo
        self.configure(fg_color=self.colorMenu)

        # Cargar la imagen del logo con fondo transparente
        self.img_logo_banco = ctk.CTkImage(light_image=Image.open(self.direccionIconoBanco), size=(200,130))
        
        # Crear el CTkLabel para el logo
        self.lbl_logo_banco = ctk.CTkLabel(self, image=self.img_logo_banco, anchor='center', text='', fg_color='transparent')
        self.lbl_logo_banco.grid(row=0, column=0, pady=5, padx=20)

        # Crear el nombre del banco
        self.nombre_banco = ctk.CTkLabel(self, text=self.nombreBanco, text_color=self.colorTextMenu, anchor='center', font=('Roboto', 24))
        self.nombre_banco.grid(row=1, column=0, padx=10, columnspan=2)

        # Espacio
        self.espacio_1 = ctk.CTkFrame(self, width=1, height=30)
        self.espacio_1.grid(row=2, column=0)

        # Botones del menú
        self.nombre_botones_menu = button_names
        self.orden_botones = 3
        self.orden_botones = 3
        self.btnsMenu = []
        for str_btn in self.nombre_botones_menu:
            btnMenu = ctk.CTkButton(
                self, 
                text=str_btn, 
                fg_color=self.colorMenu, 
                corner_radius=5, 
                height=40, 
                anchor='center', 
                text_color=self.colorTextMenu, 
                text_color_disabled=self.colorMenu,
                width=230
            )
            self.btnsMenu.append(btnMenu)

            btnMenu.grid(row=self.orden_botones, column=0, pady=5, columnspan=2)
            self.orden_botones += 1
        
        for btnMenu in self.btnsMenu:
          btnMenu.bind("<Enter>", lambda event: btnMenu.configure(text_color=self.colorMenu, fg_color=self.seleccionBoton)) 
          btnMenu.bind("<Leave>", lambda event:btnMenu.configure(text_color=self.colorTextMenu, fg_color=self.colorMenu))     

        # Espacio 2
        self.espacio_2 = ctk.CTkFrame(self, width=1, height=180)
        self.espacio_2.grid(row=self.orden_botones, column=0)

        self.orden_botones += 1

        # Botón para cerrar sesión
        self.btn_cerrar_sesion = ctk.CTkButton(
            self, 
            text=self.txtCerrarSesion, 
            fg_color=self.colorMenu, 
            text_color=self.colorTextMenu, 
            anchor='center',
            font=('Arial', 10),
            hover=False
        )

        
        self.btn_cerrar_sesion.bind("<Enter>", lambda event: 
        self.btn_cerrar_sesion.configure(font=('Arial', 12))) 
        
        self.btn_cerrar_sesion.bind("<Leave>", lambda event:
        self.btn_cerrar_sesion.configure(font=('Arial', 10)))     
        self.btn_cerrar_sesion.grid(row=self.orden_botones, column=0, pady=5)

        # Diseño auto ajustable
        self.rowconfigure(0, weight=1)
        self.nombre_banco.columnconfigure(0, weight=1)
