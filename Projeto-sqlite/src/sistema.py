from src.controllers.app_controller import Application
class Sistema:
    def __init__(self)-> None:
        self.app = Application()
        self.continuar = True
        self.acoes = {
            "0": self.sair,
            "1": self.criar_pedido,
            "2": self.exibir_itens
        }  
    
    def menu():
        print("1 - Criar novo pedido")
        print("2 - Exibir itens")
        print("3 - Adicionar item")
        print("4 - Visualizar pedido")
        print("5 - Total do Pedido")
        print("0 - Sair")
    def sair():
        global continuar 
        continuar = False
    def criar_pedido():
        global app
        cpf = input("CPF: ")
        app.criar_novo_pedido(cpf = cpf)
    def exibir_itens():
        global app
        for item in app.listar_itens():
            print(item)
    
while continuar:
    self.menu()
    opcao = input()
    if opcao not in acoes.keys():
        print("Opcao Invalida")
        continue
    acoes[opcao]()
    
    