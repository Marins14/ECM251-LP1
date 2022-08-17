class Arvore:
    def __init__(self,nome):
        self.nome = nome
    def ola(self):
        return f'Ola eu sou {self.nome}'
class Alface:
    def __init__(self,nome):
        self.nome = nome
    def ola(self):
        return f'Fala aew! Eu sou o {self.nome}'
# Verifica se o arquivo do modulo é o principal na execução 
if __name__ == "__main__":
    print('Funcionei né')