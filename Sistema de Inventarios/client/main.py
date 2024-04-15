import customtkinter as ctk
from app.app import App;
from async_tkinter_loop import async_mainloop

if __name__ == "__main__":
    try:
        root = ctk.CTk()
        app = App(root)
        async_mainloop(root)
    except Exception as e:
        pass
