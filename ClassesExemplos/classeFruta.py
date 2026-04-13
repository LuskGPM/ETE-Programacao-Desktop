class Frutas:
    def __init__(self, param_nomeFruta, param_nomeCor, param_nomeSabor):
        self.nome = param_nomeFruta
        self.cor = param_nomeCor
        self.sabor = param_nomeSabor

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Cor: {self.cor}")
        print(f"Sabor: {self.sabor}")

laranja = Frutas("Laranja", "Laranja", "Doce")
laranja.mostrar_informacoes()

"""
Output:
Nome: Laranja
Cor: Laranja
Sabor: Doce
"""