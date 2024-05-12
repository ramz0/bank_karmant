from customtkinter import *
from PIL import Image
from widgets_custom import DashboardMenuCliente

app = CTk()
app.geometry("400x400")
frame_log = CTkFrame(app, fg_color="#2B8C57")
frame_log.grid(row=0, column=0, sticky= "nswe", pady= 5, padx= 5 )

frame_log_2 = CTkFrame(app)
frame_log_2.grid(row=0, column=1, sticky= "nswe", pady= 5, padx= 5 )

img_logo = Image.open("assets/logobanco.png")
img_logobanco= CTkImage(light_image=img_logo, dark_image=img_logo, size=(200,130))

lb_logo= CTkLabel(frame_log, image=img_logobanco,text="", compound="center")
lb_logo.grid(row=0, column=0, sticky= "w",  padx= 15 )

etiqueta_titulo = CTkLabel(frame_log, text= "Bank-karmant")
etiqueta_titulo.grid(row=1, column=0)
#app.wm_attributes('-fullscreen',True)
                  
etiqueta_login = CTkLabel(frame_log_2, text="Inicio de Sesión")
etiqueta_login.grid(row=0, column=3, pady= 5, padx=5)

etiqueta_usuario = CTkLabel(frame_log_2, text="Ingresa tu usuario")
etiqueta_usuario.grid(row=1, column=3, pady= 5, padx=5)

entry_nombre_usuario = CTkEntry(frame_log_2)
entry_nombre_usuario.grid(row=2, column=3, pady= 5, padx=5)

etiqueta_pass = CTkLabel(frame_log_2, text="Ingresa tu contraseña")
etiqueta_pass.grid(row=3, column=3, pady= 5, padx=5)

entry_pass = CTkEntry(frame_log_2)
entry_pass.grid(row=4, column=3, pady= 5, padx=5)



boton= CTkButton(frame_log_2, text="Ingresar", corner_radius=32, fg_color="#2B8C57",
                hover_color="green", border_color="#FFFFFF",
                border_width=2)
boton.grid(row=8, column=3, pady= 5, padx= 5 )


app.rowconfigure(0, weight=1)  
app.columnconfigure(0, weight=10)

frame_log.rowconfigure(0, weight=1)

app.mainloop()

