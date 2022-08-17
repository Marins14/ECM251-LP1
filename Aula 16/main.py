from modelos.Documentos import Document, Email,Book
from modelos.plantas import Arvore, Alface

def run_system():
    doc1 = Document()
    doc2 = Email(authors=['Matheus Marins Bernardello'])
    doc3 = Book(authors =["Jonathan","Michelle","Gabriel"])
    print(doc2.get_authors())
    print(doc3)
    
    
if __name__ == "__main__":
    # planta1 = Arvore('Carvalho')
    # planta2 = Alface(nome='Hamburguer de siri do futuro')

    # print(planta1.ola())
    # print(planta2.ola())
    run_system()
