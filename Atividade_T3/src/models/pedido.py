# Matheus Marins Bernardello RA: 20.00286-6
class Pedido:
    def __init__(self, numero_pedido, id_cliente,carrinho, data_hora) -> None:
        self.numero_pedido = numero_pedido
        self.id_cliente = id_cliente
        self.carrinho = carrinho
        self.data_hora = data_hora

    def __str__(self) -> str:
        return f'Pedido numero: {self.numero_pedido} - Cliente: {self.id_cliente} -Data e Hora: {self.data_hora} - Carrinho: {self.carrinho}'
