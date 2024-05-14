import decimal
import tkinter as tk

import customtkinter as ctk
from customtkinter import *
from PIL import Image

<<<<<<< HEAD
=======
from ConexionMDB import ConexionMDB
>>>>>>> main
from widgets_custom import DashboardMenuCliente, MovimientoWidget

# LISTA DE LOS BOTONES QUE ESTARAN EN EL MENU:
nombreBotonesMenu = ['DEPOSITO', 'TRANSFERENCIA', 'RETIRAR']
direccion_iconoretirar = 'assets/icono_retirar.png'
<<<<<<< HEAD
direccion_movimiento_icono_ida = 'assets/icono_mv_ida.png'
direccion_movimiento_icono_llegada = 'assets/icono_mv_ida.png'
=======
>>>>>>> main

ctk.set_appearance_mode("light") # Fuerza el modo claro
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

root = ctk.CTk()
# COMO INVOCAR EL MENU DEL USUARIO
dashboard_menu = DashboardMenuCliente(root, nombreBotonesMenu, 'USUARIO')
dashboard_menu.grid(row=0, column=0,pady=5, padx=10, ipady=10,ipadx=10, sticky="wsn")

cuerpo_retirar= ctk.CTkFrame(root, fg_color='WHITE', border_width=1)
cuerpo_retirar.grid(row=0, column=1, pady=5, padx=10, ipady=10,ipadx=10, sticky="ewsn")

contenedor_head= ctk.CTkFrame(cuerpo_retirar, fg_color='#EBEBEB', border_width=1)
contenedor_head.grid(row=0, column=0, sticky='ew', pady=10, padx=10)

titulo= ctk.CTkLabel(contenedor_head,text='RETIRAR',justify="center",fg_color="transparent",font=("Arial",30))
titulo.grid(row=0, column=0, pady=5, padx=10)

img_logo_retiro = ctk.CTkImage(light_image=Image.open(direccion_iconoretirar), size=(100,100))
img = Image.open(direccion_iconoretirar)

# Redimensionar la imagen si es necesario
img_resized = img.resize((100, 100))  # Ajusta el tamaño de la imagen según lo necesario

# Crear un CTkImage con la imagen redimensionada
img_logo_retiro = ctk.CTkImage(light_image=img_resized, size=(100, 100))

# Crear un CTkLabel para mostrar la imagen
img_label = ctk.CTkLabel(contenedor_head,text="",justify="center", image=img_logo_retiro)
img_label.grid(row=1, column=0, pady=5, padx=10)

# saldo disponible
contenedor_datos= ctk.CTkFrame(cuerpo_retirar, fg_color='#EBEBEB', border_width=1)
contenedor_datos.grid(row=1, column=0, sticky='new', pady=10, padx=10)
titulo_saldo= ctk.CTkLabel(contenedor_datos,text='saldo disponible',justify="center",fg_color="transparent",font=("Arial",30))
titulo_saldo.grid(row=0, column=0, pady=5, padx=10)

#labels de la cuenta

saldo= ctk.CTkLabel(contenedor_datos,text='saldo: ',fg_color="transparent",font=("Arial",20))
saldo.grid(row=1, column=1, pady=5, padx=10,sticky="e")

#numero de cuenta
numero_cuenta= ctk.CTkLabel(contenedor_datos,text='numero de cuenta:',fg_color="transparent",font=("Arial",20))
numero_cuenta.grid(row=1, column=0, pady=5, padx=10,sticky="w")


#aqui obtiene el valor del saldo
saldo_disponible= ctk.CTkLabel(contenedor_datos,text='saldo',fg_color="transparent",font=("Arial",20))
saldo_disponible.grid(row=2, column=1, pady=5, padx=10,sticky="w")

#se obtienen valor de la cuenta
cuenta= ctk.CTkLabel(contenedor_datos,text='numero de cuenta',fg_color="transparent",font=("Arial",20))
cuenta.grid(row=2, column=0, pady=5, padx=10,sticky="w")








#retiro
contenedor_realizar_retiro= ctk.CTkFrame(cuerpo_retirar, fg_color='#EBEBEB', border_width=1)
contenedor_realizar_retiro.grid(row=2, column=0, sticky='new', pady=10, padx=10)
retirar_label= ctk.CTkLabel(contenedor_realizar_retiro,text='retiro',justify="center",fg_color="transparent",font=("Arial",30))
retirar_label.grid(row=0, column=0, pady=5, padx=10)
saldo= ctk.CTkLabel(contenedor_realizar_retiro,text='saldo que desea retirar: ',fg_color="transparent",font=("Arial",20))
saldo.grid(row=1, column=0, pady=5, padx=10,sticky="we")




monto_retiro_entry = ctk.CTkEntry(contenedor_realizar_retiro, font=("Arial", 20))
monto_retiro_entry.grid(row=3, column=0, pady=10, padx=10, sticky="")

def obtener_monto_retiro():
    monto_ingresado_str = monto_retiro_entry.get()  # Obtener el texto ingresado como cadena
    if monto_ingresado_str:
        try:
            monto_ingresado_decimal = decimal.Decimal(monto_ingresado_str)  # Convertir la cadena a Decimal
            print("Monto de Retiro (Decimal):", monto_ingresado_decimal)
            # Aquí puedes usar monto_ingresado_decimal en tu lógica de aplicación
        except decimal.InvalidOperation:
            print("Error: Entrada no válida. Ingrese un número válido.")
    else:
        print("El campo de monto de retiro está vacío.")

# Crear un botón para obtener el monto de retiro
button_obtener_monto = ctk.CTkButton(contenedor_realizar_retiro, text="Retirar", command=obtener_monto_retiro)
button_obtener_monto.grid(row=4, column=0, pady=10, padx=10, sticky="")



def funcion_menu():
    print("regresar menu")

button=ctk.CTkButton(cuerpo_retirar, text="Regresar Usuario", command=funcion_menu)

button.grid(row=3, column=0, pady=10, padx=10,sticky="es")

# DISEÑO AUTO AJUSTABLE.

#menu
root.rowconfigure(0, weight=1)  
root.columnconfigure(1, weight=10)

dashboard_menu.rowconfigure(0, weight=1)

# Configurar la expansión del contenido en el contenedor
contenedor_head.columnconfigure(0, weight=1)  # Expandir la columna para centrar el contenido
contenedor_datos.columnconfigure(0, weight=1)
contenedor_datos.rowconfigure(3, weight=10)
contenedor_realizar_retiro.columnconfigure(0, weight=1)
contenedor_realizar_retiro.rowconfigure(3, weight=10)


cuerpo_retirar.columnconfigure(0, weight=1)
cuerpo_retirar.rowconfigure(3, weight=10)
root.mainloop()