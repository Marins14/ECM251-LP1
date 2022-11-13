# Matheus Marins Bernardello RA: 20.00286-6
from models.product import Produto
from dao.jogo_dao import JogoDAO
import base64 # ele que irá resolver minha vida em questão da imagem no banco de dados

class Product_Controller():
    def __init__(self) -> None:
        self.jogos_data = JogoDAO()
        self._lista_de_produtos = self.jogos_data.get_all()
    # Demais métodos da classe
    def adicionar_a_lista(self,jogo):
        if jogo not in self._lista_de_produtos:
            self._lista_de_produtos.append(jogo)
    def criar_novo_produto(self,nome,descricao,keyword,valor,imagem):
        string_binaria = base64.b64encode(imagem.getvalue())
        construtor = base64.b64decode((string_binaria))
        aux = Produto(nome,descricao,keyword,valor,construtor)# O proprio streamlit faz a conversão binaria da imagem depois. 
        self.jogos_data.inserir_item(aux)
    def exibir_Jogos(self,jogo):
        return self._lista_de_produtos[jogo]
    def get_Jogo(self,index):
        return self._lista_de_produtos[index]
    def get_Quantidade_Jogos(self):
        return len(self._lista_de_produtos)
    def remover(self,jogo):
        if jogo in self._lista_de_produtos:
            self._lista_de_produtos.remove(jogo)