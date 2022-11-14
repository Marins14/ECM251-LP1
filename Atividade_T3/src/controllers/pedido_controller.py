# Matheus Marins Bernardello RA: 20.00286-6

from models.pedido import Pedido
from dao.pedido_dao import PedidoDAO

class Pedido_Control:
    def __init__(self) -> None:
        self.pedido_data = PedidoDAO()
        
    def inserir_pedido(self,id_cliente,carrinho,data_hora):
        try:
            numero_pedido = len(self.pedido_data.get_all())+1
            produtos = str(carrinho.printa_geral())
            valor_total = carrinho.get_Valor_Total()
            aux = Pedido(numero_pedido,id_cliente,produtos,valor_total, data_hora)
            self.pedido_data.inserir_pedido(aux)
        except:
            return False
        False

        
    