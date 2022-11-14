# Matheus Marins Bernardello RA: 20.00286-6

from models.pedido import Pedido
from dao.pedido_dao import PedidoDAO

class Pedido_Control:
    def __init__(self) -> None:
        self.pedido_data = PedidoDAO()
        self.cliente_pedido_atual = None
    def inserir_pedido(self,id_cliente,carrinho,data_hora):
        numero_pedido = len(self.pedido_data.get_all())+1
        aux = Pedido(numero_pedido,id_cliente,carrinho,data_hora)
        self.pedido_data.inserir_pedido(aux)
    # def pegar_pedido(self, numero_pedido)-> list[Pedido]:
    #     return PedidoDAO.get_instance().pegar_pedido(numero_pedido)
    # def pegar_item(self, id) -> Pedido:
    #     item = PedidoDAO.get_instance().pegar_item(id)
    #     return item
        
    # def visualizar_pedido(self):
    #     retorno = {
    #         "id_cliente":self.cliente_pedido_atual.id_cliente,
    #         "data":self.cliente_pedido_atual.data_hora,
    #         "jogos":[]
    #     }
    #     itens_pedido = self.Pedido_Control.pegar_pedido(self.cliente_pedido_atual.id)
    #     for item in itens_pedido:
    #         item_data = self.item_controller.pegar_item(item.id)
    #         retorno["items"].append({"nome":item_data.id_cliente,"carrinho": item.carrrinho})
    #     return retorno
    

        
    