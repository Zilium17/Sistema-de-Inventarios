import tkinter as tk
import customtkinter as ctk
from app.login import Login
from constants.styles import COLORS
import ctypes
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
x, y = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
w = 1300
h = 900
class App(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        self.master = master
        self.master.geometry("{}x{}+{}+{}".format(w,h,int(x/2-w/2),int(y/2-h/2)))
        self.master.title("Home")
        self.appear_login()
        ctk.CTkButton(self.master, text = "Login", command = lambda: [self.appear_login()]).pack()
        
    def appear_login(self):
        self.master.withdraw()
        self.root2 = ctk.CTkToplevel(fg_color = COLORS["color1"])
        self.login = Login(self.root2, self.master)
