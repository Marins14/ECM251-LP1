# Matheus Marins Bernardello RA: 20.00286-6
class Pedido:
    def __init__(self, numero_pedido, id_cliente,produtos,valor_total, data_hora) -> None:
        self.numero_pedido = numero_pedido
        self.id_cliente = id_cliente
        self.produtos = produtos
        self.valor_total = valor_total
        self.data_hora = data_hora

    def __str__(self) -> str:
        return f'Pedido numero: {self.numero_pedido} - Cliente: {self.id_cliente} -Data e Hora: {self.data_hora} - Produtos: {self.produtos}, Valor Total: {str(self.valor_total)}'
