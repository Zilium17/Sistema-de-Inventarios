import tkinter as tk
import customtkinter as ctk
import ctypes
import json
from constants.styles import COLORS, FONTS
from connection.socketclient import request
from async_tkinter_loop import async_handler

from PIL import Image
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
x, y = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
w = 500
h = 700
class Login(ctk.CTkFrame):
    def __init__(self, master, parent):
        ctk.CTkFrame.__init__(self, master)
        self.master = master
        self.parent = parent
        self.master.protocol("WM_DELETE_WINDOW", self.cerrar_app)
        self.master.geometry("{}x{}+{}+{}".format(w,h,int(x/2-w/2),int(y/2-h/2)))
        self.master.title("Login")
        self.master.resizable(0,0)
        self.userVar = ""
        self.passVar = ""

        self.init_widget()
    async def sendRequest(self):
        jsonR = {
            "Head": {
                "type": "read",
                "mode": "all",
                "table": "usuario"
            },
            "Body": {
                "user": self.userVar.get(),
                "password": self.passVar.get(),
            }
        }
        res = await request('192.168.0.8', 8100, jsonR)
        data = json.loads(res)
        status = data['Head']['status']
        print(status)
        if status == "200 Authorization":
            self.show_main()
        elif status == "403 No authorization":
            self.label.configure(text = data['Head']['msg'])
        
    def init_widget(self):
        myImage = ctk.CTkImage(
            light_image = Image.open("images/user.png"),
            dark_image = Image.open('images/user.png'),
            size = (150, 150)
        )
        ctk.CTkLabel(
            master = self.master,
            text = "",
            image = myImage,
        ).pack(
            side = ctk.TOP,
            fill = ctk.BOTH,
            pady = (100, 20)
        )
        ctk.CTkLabel(
            master = self.master,
            text = "Iniciar Sesión",
            font = FONTS["TitleFont"],
            text_color = COLORS["color3"],
            height = 80
        ).pack(
            side = ctk.TOP,
            fill = ctk.BOTH,
        )
        container = ctk.CTkFrame(
            self.master,
            fg_color = "transparent"
        )
        container.pack(
            side = ctk.TOP,
            fill = ctk.BOTH,
            expand = True
        )
        self.userVar = ctk.CTkEntry(
            master = container,
            width = 260,
            height = 35,
            fg_color = COLORS["color2"],
            border_color = COLORS["color2"],
            placeholder_text = "Usuario",
            font = FONTS["TextFont"],
            
        )
        self.userVar.place(
            relx = 0.5, 
            rely = 0.5, 
            anchor = tk.CENTER,
            y = -70
        )
        self.passVar = ctk.CTkEntry(
            master = container,
            width = 260,
            height = 35,
            fg_color = COLORS["color2"],
            border_color = COLORS["color2"],
            placeholder_text = "Contraseña",
            font = FONTS["TextFont"],
        )
        self.passVar.place(
            relx = 0.5, 
            rely = 0.5, 
            anchor = tk.CENTER,
            y = 0
        )
        ctk.CTkButton(
            master = container,
            text = "Entrar",
            width = 140,
            height = 45,
            fg_color = COLORS["color4"],
            hover_color = COLORS["color5"],
            command = async_handler(self.sendRequest),
            font = FONTS["TextFont"],
        ).place(
            relx = 0.5, 
            rely = 0.5, 
            anchor = tk.CENTER,
            y = 80
        )
        self.label = ctk.CTkLabel(
            master = container,
            text = "",
            font = FONTS["TextFont"],
            text_color = COLORS["false"],
            width = 140,
            height = 45,
        )
        self.label.place(
            relx = 0.5, 
            rely = 0.5, 
            anchor = tk.CENTER,
            y = 130
        )
        
    def cerrar_app(self):
        self.parent.destroy()
        
    def show_main(self):
        self.master.destroy()
        self.parent.deiconify()