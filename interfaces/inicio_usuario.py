import customtkinter as ctk
from PIL import Image
from widgets_custom import DashboardMenuCliente, MovimientoWidget

# LISTA DE LOS BOTONES QUE ESTARAN EN EL MENU:
nombreBotonesMenu = ['DEPOSITO', 'TRANSFERENCIA', 'RETIRO']
direccion_iconoCliente = 'assets/icono_cliente.png'
direccion_movimiento_icono_ida = 'assets/icono_mv_ida.png'
direccion_movimiento_icono_llegada = 'assets/icono_mv_ida.png'
iconos_movimientos = [direccion_movimiento_icono_ida, direccion_movimiento_icono_llegada]

usuario_final = "usuario"

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

nombreCliente = ctk.CTkLabel(contenedorCliente, text='Cliente:' + usuario_final)
nombreCliente.grid(row=0, column=0, pady=5, padx=35)







mensajeSaldo = ctk.CTkLabel(contenedorCliente, text='Saldo disponible')
mensajeSaldo.grid(row=1, column=1, pady=5, padx=35)

saldoDisponible = ctk.CTkLabel(contenedorCliente, text='$ 000.00')
saldoDisponible.grid(row=2, column=1, pady=5, padx=35)

lbl_movimientos = ctk.CTkLabel(curpoInterfaz, text='Movimientos:')
lbl_movimientos.grid(row=1, column=0, pady=5, padx=10, sticky='w')

contenedorMovimientosCliente = ctk.CTkScrollableFrame(curpoInterfaz, fg_color='white')
contenedorMovimientosCliente.grid(row=2, column=0, sticky='wens', pady=10, padx=10)


cardMovimiento = MovimientoWidget(contenedorMovimientosCliente, icon_path=iconos_movimientos[0], accion_text='Depósito', fecha_text='2024-05-12', usuario_text='Cliente: ' + usuario_final, cantidad_text='$100.00')
cardMovimiento.grid(row=0, column=0, sticky='we')

# DISEÑO AUTO AJUSTABLE.

#menu
root.rowconfigure(0, weight=1)  
root.columnconfigure(1, weight=10)

dashboard_menu.rowconfigure(0, weight=1)

curpoInterfaz.columnconfigure(0, weight=1)
curpoInterfaz.rowconfigure(2, weight=10)

contenedorMovimientosCliente.columnconfigure(0, weight=1)

cardMovimiento.columnconfigure(3, weight=1)

root.mainloop()