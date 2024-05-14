import decimal
import subprocess
import tkinter as tk
from tkinter import messagebox

import customtkinter as ctk
from customtkinter import *
from PIL import Image

from ConexionMDB import *
from widgets_custom import DashboardMenuCliente, MovimientoWidget

# LISTA DE LOS BOTONES QUE ESTARAN EN EL MENU:
nombreBotonesMenu = ['DEPOSITO', 'TRANSFERENCIA', 'RETIRAR']
direccion_iconoretirar = 'assets/icono_retirar.png'

conexion_db = conectar_a_MariaDB()
cursor_db = conexion_db.cursor()

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

def obtener_saldo_cuenta(numero_cuenta, label_saldo):
    query = f"SELECT SALDO FROM CUENTA WHERE NUMERO_CUENTA = '{numero_cuenta}'"
    cursor_db.execute(query)
    saldo = cursor_db.fetchone()
    if saldo:
        label_saldo.configure(text=f"Saldo: ${saldo[0]}")
    else:
        label_saldo.configure(text="Cuenta no encontrada")

def obtener_saldo():
    numero_cuenta = cuenta.get()  # Obtener el número de cuenta ingresado
    if numero_cuenta:
        obtener_saldo_cuenta(numero_cuenta, saldo_disponible)  # Pasar saldo_disponible como argumento

saldo_disponible = ctk.CTkLabel(contenedor_datos, text='saldo', fg_color="transparent", font=("Arial", 20))
saldo_disponible.grid(row=2, column=1, pady=5, padx=10, sticky="w")


# Se obtiene valor de la cuenta
cuenta = ctk.CTkEntry(contenedor_datos)
cuenta.grid(row=2, column=0, pady=5, padx=10, sticky="w")

button_obtener_saldo = ctk.CTkButton(contenedor_datos, text="Obtener Saldo", command=obtener_saldo)
button_obtener_saldo.grid(row=4, column=0, pady=10, padx=10, sticky="")







def realizar_retiro():
    numero_cuenta = cuenta.get()  # Obtener el número de cuenta ingresado

    if not numero_cuenta:
        print("Número de cuenta no ingresado.")
        return

    monto_retiro = obtener_monto_retiro()  # Obtener el monto de retito como Decimal
    
        
    if monto_retiro is None:
        print("Monto de retito inválido.")
        return
    
    

    try:
        # Obtener el saldo actual de la cuenta
        query = f"SELECT SALDO FROM CUENTA WHERE NUMERO_CUENTA = '{numero_cuenta}'"
        cursor_db.execute(query)
        saldo_actual = cursor_db.fetchone()

        if saldo_actual is None:
            print("Cuenta no encontrada.")
            return

        saldo_actual = decimal.Decimal(saldo_actual[0])
        if saldo_actual < monto_retiro:
            messagebox.showinfo("Saldo Insuficiente", "Saldo insuficiente para realizar el retiro.")
            return

        nuevo_saldo = saldo_actual - monto_retiro

        # Actualizar el saldo en la base de datos
        update_query = f"UPDATE CUENTA SET SALDO = {nuevo_saldo} WHERE NUMERO_CUENTA = '{numero_cuenta}'"
        cursor_db.execute(update_query)
        conexion_db.commit()

        # Actualizar el texto del saldo disponible en la interfaz
        saldo_disponible.configure(text=f"Saldo: ${nuevo_saldo}")

        print(f"retito de ${monto_retiro} realizado en la cuenta {numero_cuenta}.")
    except Exception as e:
        print(f"Error al realizar el retito: {str(e)}")






#retiro
contenedor_realizar_retiro= ctk.CTkFrame(cuerpo_retirar, fg_color='#EBEBEB', border_width=1)
contenedor_realizar_retiro.grid(row=2, column=0, sticky='new', pady=10, padx=10)
retirar_label= ctk.CTkLabel(contenedor_realizar_retiro,text='retiro',justify="center",fg_color="transparent",font=("Arial",30))
retirar_label.grid(row=0, column=0, pady=5, padx=10)
saldo= ctk.CTkLabel(contenedor_realizar_retiro,text='saldo que desea retirar: ',fg_color="transparent",font=("Arial",20))
saldo.grid(row=1, column=0, pady=5, padx=10,sticky="we")




monto_retiro_entry = ctk.CTkEntry(contenedor_realizar_retiro, font=("Arial", 20))
monto_retiro_entry.grid(row=3, column=0, pady=10, padx=10, sticky="")

import decimal


def obtener_monto_retiro():
    monto_ingresado_str = monto_retiro_entry.get()  # Obtener el texto ingresado como cadena
    if monto_ingresado_str:
        try:
            monto_ingresado_decimal = decimal.Decimal(monto_ingresado_str)  # Convertir la cadena a Decimal
            return monto_ingresado_decimal  # Devolver el monto como Decimal
        except decimal.InvalidOperation:
            print("Error: Entrada no válida. Ingrese un número válido.")
    else:
        print("El campo de monto de depósito está vacío.")

# Crear un botón para obtener el monto de deposito
button_obtener_monto = ctk.CTkButton(contenedor_realizar_retiro, text="retirar", command=realizar_retiro)
button_obtener_monto.grid(row=4, column=0, pady=10, padx=10, sticky="")



def funcion_menu():
    root.destroy()
    subprocess.Popen(['python','inicio_usuario.py'])

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