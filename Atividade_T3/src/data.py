# Matheus Marins Bernardello RA: 20.00286-6 
from models.product import Produto
from dao.jogo_dao import JogoDAO

data = JogoDAO()
produtos_loja = [
                    Produto("The Witcher 3: Wild Hunt","Geraldao ataca novamente!","geraldo",79.99,"./assets/geralt.png"),
                    Produto("Read Dead Redemption 2","Melhor do que nunca!","redDead",99.90,"./assets/ReadDead.jpeg"),
                    Produto("Elden Ring","Anel do Elden!","anelzin",250.00,"./assets/elden_ring.png"),
                    Produto("Grand Theft Auto 5","Sim, o 5 ainda","n att",99.99,"./assets/gta.png"),
                    Produto("Rainbow Six Siege","Aquele da série do Tom Clancy's","R6",39.99,"./assets/R6.png"),
                    Produto("Stray","Sim, um gato protagonista","gatin",59.99,"./assets/Stray.png"),
                    Produto("God Of War: Ragnarok","ELE VOLTOU!","Bom de guerra",375.00,"./assets/God_Rag.png"),
                    Produto("OverWatch 2","Não, não é de graça!","vou pagar",250.00,"./assets/overwatch.png"),
                    Produto("Outlast Trials","Todos querem esta experiência!","terror",300.00,"./assets/Out_trials.jpg")]

jogos_data = data.get_all()

for jogo in jogos_data:
    code = open(f'./img/{jogo.get_Nome().jpeg}','wb')
    code.write(jogo.get_Imagem())
    code.close()
    