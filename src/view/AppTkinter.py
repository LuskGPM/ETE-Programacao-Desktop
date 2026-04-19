import tkinter as tk

class AppTkinter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gerenciamento de usuarios")
        self.geometry("500x350")
        self.__fonte_padrao: tuple = ("Arial", 12)
        self.__fonte_grande: tuple = ("Arial", 16)
        self.__fonte_pequena: tuple = ("Arial", 8)

    def __create_widgets(self):
        tk.Label(self, text="Gerenciamento de usuarios", font=self.__fonte_grande).grid(row=0, column=0, columnspan=3, pady=10)

        tk.Label(self, text="Nome:", font=self.__fonte_padrao).grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.__entry_nome()
        tk.Label(self, text="Email:", font=self.__fonte_padrao).grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.__entry_email()

    def __entry_nome(self):
        self.entry_nome = tk.Entry(self, font=self.__fonte_padrao)
        self.entry_nome.grid(row=1, column=1, padx=5, pady=5)

    def __entry_email(self):
        self.entry_email = tk.Entry(self, font=self.__fonte_padrao)
        self.entry_email.grid(row=2, column=1, padx=5, pady=5)

    def run_app(self):
        self.__create_widgets()
        self.mainloop()