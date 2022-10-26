from src.dao.pedido_dao import PedidoDAO
from src.controllers.item_controller import ItemController
from src.models.pedido import Pedido
class PedidoController:
    def __init__(self) -> None:
        pass
    def total_pedido(self, numero_pedido)-> float:
        items_pedido = PedidoDAO.get_instance().get_itens(numero_pedido)
        total = 0
        item_controller = item_controller()
        for (item_id, quantidade) in items_pedido:
            item = item_controller.pegar_item(item_id)
            total += item.preco * quantidade
        return total
    def pegar_pedido(self, numero_pedido)-> list[Pedido]:
        return PedidoDAO.get_instance().pegar_pedido(numero_pedido)