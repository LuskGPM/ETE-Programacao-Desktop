import tkinter as tk
from model.ListaUserss import repo

class EntryList:
    def __init__(self, master):
        self.master = master

        self.listbox = tk.Listbox(self.master, font=("Arial", 12))
        self.listbox.place(x=500, y=50, width=400, height=250)  # Posiciona a lista no local desejado
    
    def create_list(self, users: list, row: int = 0, column: int = 6, font: tuple = ("Arial", 12)):
        tk.Label(self.master, text="Lista de Usuários:", font=font).place(x=500, y=20)  # Título da lista
        for user in users:
            user_info = f"{user['nome']} - {user['email']} - {user['cpf']} - {user['telefone']}"
            self.listbox.insert(tk.END, user_info)

    def update_list(self, users: list):
        self.listbox.delete(0, tk.END)  # Limpa a lista existente
        self.create_list(users)  # Cria a nova lista com os usuários atualizados

    def exclude_user(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            repo.delete_user(selected_index[0])  # Remove o usuário do repositório
            self.update_list(repo.get_users())  # Atualiza a lista de usuários na interface
    
    def __cadastrar(self, new_user: dict = None):
        repo.add_user(new_user)
        self.update_list(repo.get_users())  # Atualiza a lista de usuários na interface
        print("Usuário cadastrado:", repo.get_users()[-1])  # Exibe o último usuário cadastrado

    def submit_button(self, fonte: tuple = ("Arial", 12), row: int = 0, column: int = 0, new_user: dict = None):
        self.button_submit = tk.Button(self.master, text="Submit", font=fonte, command=lambda: self.__cadastrar(new_user))
        self.button_submit.grid(row=row, column=column+1, columnspan=2, pady=10, padx=5, ipadx=15, ipady=5)

    def delete_button(self, font: tuple = ("Arial", 12), row: int = 0, column: int = 0):
        self.button_delete = tk.Button(self.master, text="Excluir", font=font, command=self.exclude_user)
        self.button_delete.place(x=500, y=310)  # Posiciona o botão abaixo da lista