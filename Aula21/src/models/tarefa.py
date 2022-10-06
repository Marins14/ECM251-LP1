class Tarefa:
    def __init__(self,descricao,concluida = False) -> None:
        self._descricao = descricao
        self._concluida = concluida
    def get_descricao(self):
        return self._descricao
    def get_concluida(self):
        return self._concluida
    def set_concluida(self,status):
        status = self._concluida
    def __str__(self) -> str:
        return f'Tarefa[descricao:{self._descricao}]- concluida:{self._concluida}'