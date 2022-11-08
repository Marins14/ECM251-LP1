# Matheus Marins Bernardello RA: 20.00286-6 
class Carrinho():
    def __init__(self) -> None:
        self._carrinho = []
    # Demais métodos da classe
    def adicionar(self,produto):
        self._carrinho.append(produto)    
    def exibir_Produtos(self,produto):
        return self._carrinho[produto]
    def get_Valor_Total(self):
        total = 0.0
        for produto in self._carrinho:
            total += produto.get_Valor()
        return total
    def get_Quantidade_Produtos(self):
        return len(self._carrinho)
    def remover(self,produto):
        if produto in self._carrinho:
            self._carrinho.remove(produto)
    def get_Quantidade_Produtos_Repetidos(self,objetivo):
        contador = 0
        for produto in self._carrinho:
            if objetivo == produto:
                contador += 1
        return contador