import classes as cls
import customtkinter as ctk

ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk): # somethign
    def __init__(self):
        super().__init__()
        self.wm_title('Main Menu')
        self.geometry('500x500')
        self.resizable(False, False)

if __name__ == '__main__':
    App().mainloop()