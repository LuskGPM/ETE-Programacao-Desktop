import tkinter as tk
from .Campos_Aplicativo import Campos_Aplicativo

class AppTkinter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gerenciamento de usuarios")
        self.geometry("960x540")

        self.Entry_Labels = Campos_Aplicativo(self)
        self.__fonte_padrao: tuple = ("Arial", 16)
        self.__fonte_grande: tuple = ("Arial", 20)
        self.__fonte_pequena: tuple = ("Arial", 10)

    def __create_widgets(self) -> None:
        tk.Label(self, text="Gerenciamento de usuarios", font=self.__fonte_grande).grid(row=0, column=0, columnspan=3, pady=10)
        tk.Label(self, text="Preencha os campos abaixo:", font=self.__fonte_padrao).grid(row=1, column=0, columnspan=3, pady=5)
        self.Entry_Labels.createNomeEntry(self.__fonte_padrao, row=2, column=0)
        self.Entry_Labels.createEmailEntry(self.__fonte_padrao, row=3, column=0)
        self.Entry_Labels.createCPFEntry(self.__fonte_padrao, row=4, column=0)
        self.Entry_Labels.createTelefoneEntry(self.__fonte_padrao, row=5, column=0)
        self.Entry_Labels.submit_button(self.__fonte_padrao, row=6, column=0)
        self.Entry_Labels.create_list([])
        self.Entry_Labels.delete_button(self.__fonte_pequena, row=0, column=0)

    def run_app(self):
        self.__create_widgets()
        self.mainloop()