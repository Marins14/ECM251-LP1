# Matheus Marins Bernardello RA: 20.00286-6
from cgi import print_exception
from unicodedata import name

class Produto():
    # Método construtor
    def __init__(self,nome,descricao,keyword,valor,imagem = None):
        self._nome = nome
        self._descricao = descricao
        self._keyword = keyword
        self._valor = valor
        self._imagem = imagem
    # Getters p facilitar nossa vida depois
    def get_Nome(self):
        return self._nome
    def get_Descricao(self):
        return self._descricao
    def get_Keyword(self):
        return self._keyword
    def get_Valor(self):
        return self._valor
    def get_Imagem(self):
        return self._imagem
    # Faz com que o item print de forma especifica
    def __str__(self) -> str:
        return self._nome + " - R$ "+ str(self._valor)
    # Compara itens
    def __eq__(self, __o: object) -> bool:
        if(isinstance(__o,Produto)):
            return self._nome == __o.get_Nome()
        return False