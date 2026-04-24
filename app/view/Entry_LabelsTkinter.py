import tkinter as tk
from model.ListaUserss import UserRepo

class Entry_LabelsFormulario():
    def __init__(self, master):
        self.master = master

    def createNomeEntry(self, fonte: tuple = ("Arial", 12), row: int = 0, column: int = 0):
        tk.Label(self.master, text="Nome:", font=fonte).grid(row=row, column=column, sticky="e", padx=5, pady=5)
        self.entry_nome = tk.Entry(self.master, font=fonte)
        self.entry_nome.grid(row=row, column=column+1, padx=5, pady=5, ipady=5)

    def createEmailEntry(self, fonte: tuple = ("Arial", 12), row: int = 0, column: int = 0):
        tk.Label(self.master, text="Email:", font=fonte).grid(row=row, column=column, sticky="e", padx=5, pady=5)
        self.entry_email = tk.Entry(self.master, font=fonte)
        self.entry_email.grid(row=row, column=column+1, padx=5, pady=5, ipady=5)

    def createCPFEntry(self, fonte: tuple = ("Arial", 12), row: int = 0, column: int = 0):
        tk.Label(self.master, text="CPF:", font=fonte).grid(row=row, column=column, sticky="e", padx=5, pady=5)
        self.entry_cpf = tk.Entry(self.master, font=fonte)
        self.entry_cpf.grid(row=row, column=column+1, padx=5, pady=5, ipady=5)

    def createTelefoneEntry(self, fonte: tuple = ("Arial", 12), row: int = 0, column: int = 0):
        tk.Label(self.master, text="Telefone:", font=fonte).grid(row=row, column=column, sticky="e", padx=5, pady=5)
        self.entry_telefone = tk.Entry(self.master, font=fonte)
        self.entry_telefone.grid(row=row, column=column+1, padx=5, pady=5, ipady=5)



