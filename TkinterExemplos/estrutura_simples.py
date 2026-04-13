import tkinter as tk

janela = tk.Tk()
janela.title("Estrutura Simples")
janela.geometry("300x400")

tk.Label(janela, text="Olá, Mundo!").pack(fill="x")
tk.Button(janela, text="Clique Aqui", command=lambda: print("Botão clicado!")).pack(side="left")
tk.Button(janela, text="Sair", command=janela.quit).pack(side="right")
tk.Entry(janela).pack(pady=10)
tk.Label(janela, text="Tkinter é fácil de usar!").pack(side="bottom")

janela.mainloop()

# Opções Uteis: side="top" | "bottom" | "left" | "right"
# fill="x" | "y" | "both"
# expand=True