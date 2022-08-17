from modelos.Documentos import Document, Email,Book
from modelos.plantas import Arvore, Alface

def run_system():
    doc1 = Document()
    doc2 = Email(to='20.00286-6@maua.br',authors=['Matheus Marins Bernardello'])
    doc3 = Book(title= "Galerinha", authors =["Jonathan","Michelle","Gabriel"])
    print(doc2)
    print(doc3)
    
    
if __name__ == "__main__":
    # planta1 = Arvore('Caralho')
    # planta2 = Alface(nome='Hamburguer de siri do futuro')

    # print(planta1.ola())
    # print(planta2.ola())
    run_system()
