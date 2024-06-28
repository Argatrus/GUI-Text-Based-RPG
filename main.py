import combat_engine as ce
import customtkinter as ctk

ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk): # Main Menu
    def __init__(self):
        super().__init__()
        self.wm_title('Main Menu')
        self.geometry('500x500')
        self.resizable(False, False)
        self.button1 = ctk.CTkButton(self, text='Combat engine', command=self.combat_engine)
        self.button1.pack()
    
    def combat_engine(self):
        ce.App().mainloop()

if __name__ == '__main__':
    App().mainloop()