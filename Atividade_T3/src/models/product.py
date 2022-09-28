from cgi import print_exception
from unicodedata import name

class Product():
    def __init__(self,name,descricao,keyword,price,url) -> None:
        self._name = name
        self._descricao = descricao
        self._keyword = keyword
        self._price = price 
        self._url = url
    # Getters da classe
    def get_Nome(self):
        return self._name
    def get_Descricao(self):
        return self._descricao
    def get_Keyword(self):
        return self._keyword
    def get_Valor(self):
        return self._price
    def get_Imagem(self):
        return self._url
     # Faz com que o item print de forma especifica
    def __str__(self) -> str:
        return self._name + " - R$ "+ str(self._price)
    def __eq__(self,__o:object) -> bool:
        if(isinstance(__o,Product)):
             return self._name == __o.get_Nome()
        return False