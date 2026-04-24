import tkinter as tk
from model.ListaUserss import repo

class Campos_Aplicativo():
    def __init__(self, master):
        self.master = master

    # ------------------------------- LISTBOX É INSTÂNCIADA NO CONSTRUTOR DA CLASSE -------------------------------
    # ------------------------------- POIS É UM WIDGET QUE ALTERA SEU VALOR AUTOMATICAMENTE -------------------------------

        self.listbox = tk.Listbox(self.master, font=("Arial", 12))
        self.listbox.place(x=500, y=50, width=400, height=250) 

    # ------------------------------- MÉTODOS PARA CRIAR COMPONENTES NA TELA -------------------------------

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
    
    def create_list(self, users: list, font: tuple = ("Arial", 12)):
        tk.Label(self.master, text="Lista de Usuários:", font=font).place(x=500, y=20)  # Título da lista
        for user in users:
            user_info = f"{user['nome']} - {user['email']} - {user['cpf']} - {user['telefone']}"
            self.listbox.insert(tk.END, user_info)

    # ------------------------------- FIM DOS MÉTODOS PARA CRIAR COMPONENTES NA TELA -------------------------------

    # ------------------------------- MÉTODO PARA CADASTRAR -------------------------------
    def __cadastrar(self):
        # CRIA UM DICIONÁRIO COM OS DADOS DO USUÁRIO
        new_user = {
            "nome": self.entry_nome.get(),
            "email" : self.entry_email.get(),
            "cpf" : self.entry_cpf.get(),
            "telefone" : self.entry_telefone.get()
        }
        repo.add_user(new_user)
        self.update_list(repo.get_users())  # Atualiza a lista de usuários na interface
        print("Usuário cadastrado:", repo.get_users()[-1])  # Exibe o último usuário cadastrado

    def update_list(self, users: list):
        self.listbox.delete(0, tk.END)  # Limpa a lista existente
        self.create_list(users)  # Cria a nova lista com os usuários atualizados

    def exclude_user(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            repo.delete_user(selected_index[0])  # Remove o usuário do repositório
            self.update_list(repo.get_users())  # Atualiza a lista de usuários na interface

    # ------------------------------- MÉTODOS PARA A CRIAÇÃO DOS BOTÕES DE ADICIONAR E DELETAR -------------------------------
    
    def submit_button(self, fonte: tuple = ("Arial", 12), row: int = 0, column: int = 0):
        self.button_submit = tk.Button(self.master, text="Submit", font=fonte, command=self.__cadastrar) # AO CLICAR NO BOTÃO, CHAMA A FUNÇÃO "__cadastrar"
        self.button_submit.grid(row=row, column=column+1, columnspan=2, pady=10, padx=5, ipadx=15, ipady=5)

    def delete_button(self, font: tuple = ("Arial", 12), row: int = 0, column: int = 0):
        self.button_delete = tk.Button(self.master, text="Excluir", font=font, command=self.exclude_user)
        self.button_delete.place(x=500, y=310)  # Posiciona o botão abaixo da lista
