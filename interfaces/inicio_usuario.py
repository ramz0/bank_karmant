import customtkinter as ctk
from widgets_custom import DashboardMenuCliente 


nombreBotonesMenu = ['DEPOSITO', 'TRANSFERENCIA', 'RETIRO']

root = ctk.CTk()

dashboard_menu = DashboardMenuCliente(root)
dashboard_menu.grid(row=0, column=0,pady=5, padx=10, ipady=10,ipadx=10, sticky="wsn")

# DISEÑO AUTO AJUSTABLE.
dashboard_menu.rowconfigure(0, weight=1)

root.rowconfigure(0, weight=1)  
root.columnconfigure(0, weight=1)

root.mainloop()