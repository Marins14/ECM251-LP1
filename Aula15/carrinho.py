class Carrinho():
    #Método construtor
    def __init__(self):
        self._itens = [] #_priva algo
    #Demais métodos da classe
    def get_valor_total(self):
        total = 0
        for item in self._itens:
            total += item.get_valor()
        return total
    def get_quantidade_itens(self):
        return len(self._itens)
    def adicionar(self, item):
        return self._itens.append(item)  
    def remover(self, item):
        pass
