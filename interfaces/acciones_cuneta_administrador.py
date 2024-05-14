from PIL import Image
import customtkinter as ctk
from widgets_custom import DashboardMenuCliente
from widgets_custom import CTkTable
from ConexionMDB import *


# LISTA DE LOS BOTONES QUE ESTARAN EN EL MENU:
nombreBotonesMenu = ['ACCIONES CUENTA', 'VISUALIZACIÓN\n ADMINISTRADOR', '']
btnsCRUD = ['   INSERTAR', '   ELIMINAR', '   ACTUALIZAR']

iconosCRUD = ['assets/icono_insert.png', 'assets/icono_delete.png', 'assets/icono_update.png']

colorBase = '#2B8C57'

tamanoIconosCRUD = (45,45)

camposTabla=['NUMERO_CUENTA','ID_CLIENTE','ID_TIPO_CUENTA','SALDO','FECHA_EMISION', 'FECHA_VENCIMIENTO']

registrosTablaCliente = select('cuenta')
registrosTablaCliente.insert(0, camposTabla)

ctk.set_appearance_mode("light") # Fuerza el modo claro
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

root = ctk.CTk()
# COMO INVOCAR EL MENU DEL USUARIO
dashboard_menu = DashboardMenuCliente(root, nombreBotonesMenu, 'ADMINISTRADOR')
dashboard_menu.grid(row=0, column=0,pady=5, padx=10, ipady=10,ipadx=10, sticky="wsn")

curpoInterfaz = ctk.CTkFrame(root, fg_color='white')
curpoInterfaz.grid(row=0, column=1, pady=5, padx=10, ipady=10,ipadx=10, sticky="ewsn")

labelTitulo = ctk.CTkLabel(curpoInterfaz, text='Operaciones', font=('Roboto', 20), text_color=colorBase)
labelTitulo.grid(row=0, column=0, pady=30, padx=25, sticky="w")

contenedorBotones = ctk.CTkFrame(curpoInterfaz, fg_color='transparent')
contenedorBotones.grid(row=1, column=0, padx=10, sticky="we")
i = 0
for tituloCRUD in btnsCRUD:
  img_icon_btnCRUD = ctk.CTkImage(light_image=Image.open(iconosCRUD[i]), size=tamanoIconosCRUD)

  btnCRUD = ctk.CTkButton(
    contenedorBotones, 
    fg_color=colorBase, 
    image=img_icon_btnCRUD, 
    text=tituloCRUD, 
    height=50,
    font=('Roboto', 15)
  )
  btnCRUD.grid(row=0, column=i, pady=10, padx=5,ipady=5, sticky="we")
  i += 1

contenedorFormInsertar = ctk.CTkFrame(curpoInterfaz, height=5, fg_color='#EFF0F0')
contenedorFormInsertar.grid(row=2, column=0, padx=20, pady=10, sticky='we')

labelTituloFormCliente=ctk.CTkLabel(contenedorFormInsertar, text='    INSERTA UNA NUEVA CUENTA:', text_color='white', fg_color=colorBase, anchor='w')
labelTituloFormCliente.grid(row=0, column=0, columnspan=6, sticky="we")

columna = 0
fila = 1
for campo in camposTabla:
  if columna == 6:
    fila += 1
    columna = 0
  labelFromInsertar = ctk.CTkLabel(contenedorFormInsertar, text= campo + ": ", text_color=colorBase, font=('Arial', 11))
  labelFromInsertar.grid(row=fila, column=columna, pady=10, padx=3, sticky="e")
  columna += 1

  entryDatoCliente = ctk.CTkEntry(contenedorFormInsertar, corner_radius=50, fg_color='white', border_width=0)
  entryDatoCliente.grid(row=fila, column=columna, pady=10, padx=3, sticky="w")
  contenedorFormInsertar.columnconfigure(columna, weight=1)
  columna += 1

contenedorForm_A_E = ctk.CTkFrame(curpoInterfaz, height=5, fg_color='transparent')
contenedorForm_A_E.grid(row=3, column=0, padx=20, pady=10, sticky='we')

contenedorFormActualizar = ctk.CTkFrame(contenedorForm_A_E, height=5, fg_color='#EFF0F0')
contenedorFormActualizar.grid(row=0, column=0, padx=20, pady=10, sticky='we')

labelFromActualizar=ctk.CTkLabel(contenedorFormActualizar, text='    ACTUALIZA UNA CUENTA:', text_color='white', fg_color=colorBase, anchor='w')
labelFromActualizar.grid(row=0, column=0, columnspan=3, sticky="we")

labelFromActualizarS = ctk.CTkLabel(contenedorFormActualizar, text= "NUEVO VALOR(set): ", text_color=colorBase, font=('Arial', 11))
labelFromActualizarS.grid(row=1, column=0, pady=10, padx=3, sticky="e")

entryDatoActualizarS = ctk.CTkEntry(contenedorFormActualizar, corner_radius=50, fg_color='white', border_width=0)
entryDatoActualizarS.grid(row=1, column=1, pady=10, padx=3, sticky="w")

cboxCampoActualizarS = ctk.CTkComboBox(contenedorFormActualizar, values=camposTabla, button_color=colorBase)
cboxCampoActualizarS.grid(row=1, column=2, pady=10, padx=8, sticky="w")

labelFromActualizarW = ctk.CTkLabel(contenedorFormActualizar, text= "DEL CAMPO(where): ", text_color=colorBase, font=('Arial', 11))
labelFromActualizarW.grid(row=2, column=0, pady=10, padx=3, sticky="e")

entryDatoAtualizarW = ctk.CTkEntry(contenedorFormActualizar, corner_radius=50, fg_color='white', border_width=0)
entryDatoAtualizarW.grid(row=2, column=1, pady=10, padx=3, sticky="w")

cboxCampoActualizarW = ctk.CTkComboBox(contenedorFormActualizar, values=camposTabla, button_color=colorBase)
cboxCampoActualizarW.grid(row=2, column=2, pady=10, padx=8, sticky="w")

contenedorFormEliminar = ctk.CTkFrame(contenedorForm_A_E, height=5, fg_color='#EFF0F0')
contenedorFormEliminar.grid(row=0, column=1, padx=20, pady=10, sticky='we')

labelFromActualizar=ctk.CTkLabel(contenedorFormEliminar, text='    ELIMINA UNA CUENTA:', text_color='white', fg_color=colorBase, anchor='w')
labelFromActualizar.grid(row=0, column=0, columnspan=6, sticky="we")

labelFromEliminarM1 = ctk.CTkLabel(contenedorFormEliminar, text= "EL DATO: ", text_color=colorBase, font=('Arial', 11))
labelFromEliminarM1.grid(row=1, column=0, pady=10, padx=3, sticky="e")

entryDatoEliminar = ctk.CTkEntry(contenedorFormEliminar, corner_radius=50, fg_color='white', border_width=0)
entryDatoEliminar.grid(row=1, column=1, pady=10, padx=3, sticky="w")

labelFromEliminarM2 = ctk.CTkLabel(contenedorFormEliminar, text= "DEL CAMPO: ", text_color=colorBase, font=('Arial', 11))
labelFromEliminarM2.grid(row=1, column=2, pady=10, padx=3, sticky="e")

cboxCampoEliminar = ctk.CTkComboBox(contenedorFormEliminar, values=camposTabla, button_color=colorBase)
cboxCampoEliminar.grid(row=1, column=3, pady=10, padx=8, sticky="w")

contenedorMovimientosCliente = ctk.CTkScrollableFrame(curpoInterfaz, fg_color='white')
contenedorMovimientosCliente.grid(row=4, column=0, sticky='wens', pady=20, padx=20)

tablaCliente = CTkTable(contenedorMovimientosCliente, header_color=colorBase, values=registrosTablaCliente)
tablaCliente.grid(row=0, column=0, sticky='we')

# DISEÑO AUTO AJUSTABLE.

#menu
root.rowconfigure(0, weight=1)  
root.columnconfigure(1, weight=10)

curpoInterfaz.columnconfigure(0, weight=1)
curpoInterfaz.rowconfigure(4, weight=1)

contenedorBotones.columnconfigure(0, weight=1)
contenedorBotones.columnconfigure(1, weight=1)
contenedorBotones.columnconfigure(2, weight=1)

contenedorMovimientosCliente.columnconfigure(0, weight=1)

root.mainloop()