import subprocess
from customtkinter import *
import PIL
from widgets_custom import DashboardMenuCliente
from subprocess import *
from tkinter import messagebox
import mysql.connector


db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bank_karmant"
)

app = CTk()
app.geometry("460x400")

frame_log = CTkFrame(app, fg_color="#2B8C57")
frame_log.grid(row=0, column=0, sticky="nswe", pady=5, padx=5)

frame_log_2 = CTkFrame(app)
frame_log_2.grid(row=0, column=1, sticky="nswe", pady=5, padx=5)

img_logo = PIL.Image.open("assets/logobanco.png")
img_logobanco = CTkImage(light_image=img_logo, dark_image=img_logo, size=(200, 130))

lb_logo = CTkLabel(frame_log, image=img_logobanco, text="", compound="center")
lb_logo.grid(row=0, column=0, sticky="we", padx=15)

etiqueta_titulo = CTkLabel(frame_log, text="Bank-karmant")
etiqueta_titulo.grid(row=1, column=0)

etiqueta_login = CTkLabel(frame_log_2, text="Inicio de Sesión", anchor="center")
etiqueta_login.grid(row=0, column=3, pady=5, padx=5)

etiqueta_usuario = CTkLabel(frame_log_2, text="Ingresa tu usuario")
etiqueta_usuario.grid(row=1, column=3, pady=5, padx=5)

entry_nombre_usuario = CTkEntry(frame_log_2)
entry_nombre_usuario.grid(row=2, column=3, pady=5, padx=20, sticky="we")

etiqueta_pass = CTkLabel(frame_log_2, text="Ingresa tu contraseña")
etiqueta_pass.grid(row=3, column=3, pady=5, padx=5)

entry_pass = CTkEntry(frame_log_2)
entry_pass.grid(row=4, column=3, pady=5, padx=20, sticky="we")

def iniciar_sesion():
    usuario_ingresado = entry_nombre_usuario.get()
    contraseña_ingresada = entry_pass.get()

    cursor = db_connection.cursor()
    query = """
            SELECT CASE 
                WHEN COUNT(*) > 0 THEN 'Aceptado'
                ELSE 'Rechazado'
            END AS mensaje
            FROM CLIENTE
            WHERE CORREO = %s AND PASSWORD = %s;
            """
    cursor.execute(query, (usuario_ingresado, contraseña_ingresada))
    resultado = cursor.fetchone()[0]  # Aquí obtenemos el resultado de la consulta

    # Después de la verificación del inicio de sesión exitoso para el cliente
    if resultado == 'Aceptado':
        messagebox.showinfo("Inicio correcto", "Se inició correctamente")
        set_usuario_final(usuario_ingresado)
        # Ocultar la pestaña
        app.destroy()
        subprocess.Popen(['python', 'inicio_usuario.py'])

    # Después de la verificación del inicio de sesión exitoso para el administrador
    elif usuario_ingresado == "admin" and contraseña_ingresada == "123":
        messagebox.showinfo("inicio correcto","se inicio correctamente")
        # Ocultar la pestaña
        app.destroy()
        subprocess.Popen(['python', 'menu_administrador.py'])
    else:
        messagebox.showerror("Error de Inicio de Sesión", "Usuario o contraseña incorrectos")





boton = CTkButton(frame_log_2, text="Ingresar", corner_radius=32, fg_color="#2B8C57",
                   hover_color="green", border_color="#FFFFFF",
                   border_width=2, width=200, height=50, command=iniciar_sesion)
boton.grid(row=5, column=3, pady=5, padx=5)



app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=6)
app.columnconfigure(1, weight=4)
frame_log.rowconfigure(0, weight=1)
frame_log_2.rowconfigure(0, weight=1)
frame_log_2.columnconfigure(3, weight=1)
frame_log_2.rowconfigure(5, weight=3)

app.mainloop()