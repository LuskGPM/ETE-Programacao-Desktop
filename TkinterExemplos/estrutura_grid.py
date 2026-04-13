import tkinter as tk

root = tk.Tk()

tk.Label(root, text="Nome").grid(row=0, column=0)
tk.Entry(root).grid(row=0, column=1)

tk.Label(root, text="Senha").grid(row=1, column=0)
tk.Entry(root).grid(row=1, column=1)

tk.Button(root, text="Login").grid(row=2, column=0, columnspan=2)

root.mainloop()

# row / column: Define a posição do widget na grade
# columnspan: Permite que o widget ocupe várias colunas
# rowspan: Permite que o widget ocupe várias linhas
# sticky: Alinha o widget dentro da célula (N, S, E, W)