from cgi import print_exception
from unicodedata import name


class Product():
    def __init__(self,name,descricao,price,url) -> None:
        self.name = name
        self.descricao = descricao
        self.price = price 
        self.url = url
    def __str__(self) -> str:
        return f'Product(name):{self.name},descricao:{self.descricao} price:{self.price}, url:{self.url}'