from tkinter import Toplevel

import pymysql


class ConexionMDB():
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='bank_karmant'
        )

        self.cursor=self.connection.cursor()
        self.cursor(print ("conexion establecida con exito"))

