import tkinter as tk
from .Entry_LabelsTkinter import Entry_LabelsFormulario
from .Entry_ListUser import EntryList

class AppTkinter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gerenciamento de usuarios")
        self.geometry("960x540")

        self.Entry_Labels = Entry_LabelsFormulario(self)
        self.Entry_List = EntryList(self)
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
        self.Entry_List.submit_button(self.__fonte_padrao, row=6, column=0, new_user=self.create_user_obt())
        self.Entry_List.create_list([])
        self.Entry_List.delete_button(self.__fonte_pequena, row=0, column=0)

    def create_user_obt(self):
        new_user = {
            "nome": self.Entry_Labels.entry_nome.get(),
            "email": self.Entry_Labels.entry_email.get(),
            "cpf": self.Entry_Labels.entry_cpf.get(),
            "telefone": self.Entry_Labels.entry_telefone.get()
        }
        return new_user

    def run_app(self):
        self.__create_widgets()
        self.mainloop()