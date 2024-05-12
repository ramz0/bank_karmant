from PIL import Image
import customtkinter as ctk
from widgets_custom import DashboardMenuCliente 

# LISTA DE LOS BOTONES QUE ESTARAN EN EL MENU:
nombreBotonesMenu = ['DEPOSITO', 'TRANSFERENCIA', 'RETIRO']
direccion_iconoCliente = 'assets/icono_cliente.png'

ctk.set_appearance_mode("light") # Fuerza el modo claro
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

root = ctk.CTk()
# COMO INVOCAR EL MENU DEL USUARIO
dashboard_menu = DashboardMenuCliente(root, nombreBotonesMenu, 'USUARIO')
dashboard_menu.grid(row=0, column=0,pady=5, padx=10, ipady=10,ipadx=10, sticky="wsn")

curpoInterfaz = ctk.CTkFrame(root, fg_color='white')
curpoInterfaz.grid(row=0, column=1, pady=5, padx=10, ipady=10,ipadx=10, sticky="ewsn")

contenedorCliente = ctk.CTkFrame(curpoInterfaz, fg_color='#EBEBEB', border_width=1)
contenedorCliente.grid(row=0, column=0, sticky='we', pady=10, padx=10)

img_logo_cliente = ctk.CTkImage(light_image=Image.open(direccion_iconoCliente), size=(100,100))

lbl_logo_banco = ctk.CTkLabel(contenedorCliente, image=img_logo_cliente, anchor='center', text='', fg_color='transparent')
lbl_logo_banco.grid(row=1, column=0, pady=5, padx=20, rowspan=2)

nombreCliente = ctk.CTkLabel(contenedorCliente, text='Cliente')
nombreCliente.grid(row=0, column=0, pady=5, padx=35)

mensajeSaldo = ctk.CTkLabel(contenedorCliente, text='Saldo disponible')
mensajeSaldo.grid(row=1, column=1, pady=5, padx=35)

saldoDisponible = ctk.CTkLabel(contenedorCliente, text='$ 000.00')
saldoDisponible.grid(row=2, column=1, pady=5, padx=35)

contenedorMovimientosCliente = ctk.CTkScrollableFrame(curpoInterfaz)
contenedorMovimientosCliente.grid(row=1, column=0, sticky='wens', pady=10, padx=10)
# DISEÑO AUTO AJUSTABLE.

#menu
root.rowconfigure(0, weight=1)  
root.columnconfigure(1, weight=10)

dashboard_menu.rowconfigure(0, weight=1)

curpoInterfaz.columnconfigure(0, weight=1)
curpoInterfaz.rowconfigure(1, weight=10)

root.mainloop()