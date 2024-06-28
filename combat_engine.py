import classes as cls
import customtkinter as ctk

ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk): # Main Menu
    def __init__(self):
        super().__init__()
        self.wm_title('Combat Engine')
        self.geometry('500x500')
        self.resizable(False, False)

