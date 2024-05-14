import subprocess
from customtkinter import *
from PIL import Image
from widgets_custom import DashboardMenuCliente
from subprocess import *

app = CTk()
app.geometry()

frame_head=CTkFrame(app, fg_color="#2B8C57")
frame_head.grid(row=0, column=0, sticky= "ne", pady= 5, padx= 5)

img_logo = Image.open("assets/logobanco.png")
img_logobanco= CTkImage(light_image=img_logo, dark_image=img_logo, size=(200,150))

lb_logo= CTkLabel(frame_head, image=img_logobanco,text="", compound="center")
lb_logo.grid(row=1, column=0, sticky= "nswe",  padx= 15 )

etiqueta_titulo = CTkLabel(frame_head, text= "Bank-karmant")
etiqueta_titulo.grid(row=2, column=0)

boton= CTkButton(frame_head, text="Cerrar Sesión", corner_radius=32, fg_color="#2B8C57",
                hover_color="green", border_color="#FFFFFF",
                border_width=2, width=150, height=50 )
boton.grid(row=1, column=5, pady= 50, padx= 50 )

lb_menu=CTkLabel(frame_head,font=("Helvetica", 50) , text="Menú")
lb_menu.grid(row=1, column=4, padx= 200)


###################################

frame=CTkFrame(app, fg_color="#FFFFFF")
frame.grid(row=1, column=0, sticky= "nswe", pady= 5, padx= 5)

img_logo_ad = Image.open("assets/menu_ad.png")
img_logo_admin= CTkImage(light_image=img_logo_ad, dark_image=img_logo_ad, size=(150,150))

lb_logo_admin= CTkLabel(frame, image=img_logo_admin, text="")
lb_logo_admin.grid(row=1, column=1, sticky= "nswe",pady=100, padx= 100)

def acciones_cuenta():
    # Código para mostrar la interfaz de acciones de cuenta
    app.destroy()
    subprocess.Popen(['python', 'acciones_cuneta_administrador.py'])

def visualizacion_administrador():
     # Código para mostrar la interfaz de acciones de cuenta
    app.destroy()
    subprocess.Popen(['python', 'vizualizacion_administrador.py'])

boton= CTkButton(frame, text="Acciones de Cuenta", corner_radius=32, fg_color="#2B8C57",
                hover_color="green", border_color="#FFFFFF",
                border_width=2, width=150, height=50, command= acciones_cuenta)
boton.grid(row=1, column=2, padx= 200 )


boton= CTkButton(frame, text="Visualización", corner_radius=32, fg_color="#2B8C57",
                hover_color="green", border_color="#FFFFFF",
                border_width=2, width=150, height=50, command=visualizacion_administrador )
boton.grid(row=2, column=2, padx= 200 )


app.mainloop()
