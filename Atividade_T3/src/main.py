# Matheus Marins Bernardello RA: 20.00286-6
import streamlit as st
from random import randint
from models.product import Product
from models.carrinho import Carrinho

if "carrinho" not in st.session_state:
    st.session_state["carrinho"] = Carrinho()
if "catalogo" not in st.session_state:

    st.session_state["catalogo"] = [
                                    Product("The Witcher 3: Wild Hunt","Geraldao ataca novamente!","geraldo",79.99,"./assets/geralt.png"),
                                    Product("Read Dead Redemption 2","Melhor do que nunca!","redDead",99.90,"./assets/ReadDead.jpeg"),
                                    Product("Elden Ring","Anel do Elden!","anelzin",250.00,"./assets/elden_ring.png"),
                                    Product("Grand Theft Auto 5","Sim, o 5 ainda","n att",99.99,"./assets/gta.png"),
                                    Product("Rainbow Six Siege","Aquele da série do Tom Clancy's","R6",39.99,"./assets/R6.png"),
                                    Product("Stray","Sim, um gato protagonista","gatin",59.99,"./assets/Stray.png"),
                                    Product("God Of War: Ragnarok","ELE VOLTOU!","Bom de guerra",375.00,"./assets/God_Rag.png"),
                                    Product("OverWatch 2","Não, não é de graça!","vou pagar",250.00,"./assets/overwatch.png"),
                                    Product("Outlast Trials","Todos querem esta experiência!","terror",300.00,"./assets/Out_trials.jpg")]

st.set_page_config(page_title="Geraldão_Store",layout="centered",initial_sidebar_state="collapsed",menu_items=None)

def check_password():
    """Returns `True` if the user had a correct password."""
    
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input(label="Digite seu E-mail:", key="username")
        st.text_input(label="Digite sua Senha:", type="password", key="password")
        col1,col2 = st.columns(spec=[1,10],gap="small")
        with col1:    
            if st.button(label="Login"):
                password_entered()
        with col2:
            if st.button(label="Esqueci a senha"):
                st.write("Redirecionando...")
        return False
    
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(label="Digite seu E-mail:", key="username")
        st.text_input(label="Digite sua Senha:", type="password", key="password")
        col1,col2 = st.columns(spec=[1,10],gap="small")
        with col1:    
            if st.button(label="Login"):
                password_entered()
        with col2:
            if st.button(label="Esqueci a senha"):
                st.write("Calma aew, to no processo aqui...")
            # Botão sem função por enquanto, aguarde novas atualizações...    
        st.error("ERRROUUU 🤣")
        return False
    
    else:
        # Password correct.
        return True

if check_password():
    home,carrinho = st.tabs(["Home","Carrinho"])
    
    with home:
        st.subheader("Temos algumas novidades, confira! 😎")
        st.subheader("Destaques 🤪")
        c1,c2,c3 = st.columns(3,gap="small")
        c4,c5,c6 = st.columns(3,gap="small")
        c7,c8,c9 = st.columns(3,gap="small")
        colunas = [c1,c2,c3,c4,c5,c6,c7,c8,c9]
        var = 0
        for coluna in colunas:
            with coluna:
                st.image(st.session_state["catalogo"][var].get_Imagem(),"R$ "+ str(st.session_state["catalogo"][var].get_Valor()))
                st.write(st.session_state["catalogo"][var].get_Descricao())
                if st.button("Adicionar ao carrinho",key=st.session_state["catalogo"][var].get_Keyword()):
                    st.write("Produto adicionado ao carrinho!")
                    st.session_state["carrinho"].adicionar(st.session_state["catalogo"][var])
                var += 1  
        st.markdown('**_Estamos preparando algo maior ainda,tenha paciência meu pupilo!_**.😴')
        st.markdown('**Geraldão_Store é uma marca registrada. Todos os direitos reservados**.')            
                
    with carrinho:
        col1,col2,col3 = st.columns([1.5,5,2.5],gap = "small")
        with col1:
            st.write("Remover: ")
            contador = 0
            while contador < st.session_state["carrinho"].get_Quantidade_Itens():
                aux = st.session_state["carrinho"].exibir_Itens(contador)
                if st.button("Remover",key = ("Remover_"+aux.get_Keyword()+str(contador))):
                     st.session_state["carrinho"].remover(aux)
                contador += 1  
        with col2:
            st.write("Itens:")
            i = 0
            while i < st.session_state["carrinho"].get_Quantidade_Itens():
                st.write(str(st.session_state["carrinho"].exibir_Itens(i)))
                i+=1
        with col3:
            st.write("Confere quant. e valor:")
            st.write("Quantidade Total: "+str(st.session_state["carrinho"].get_Quantidade_Itens()))
            st.write("Valor total: R$ "+str(st.session_state["carrinho"].get_Valor_Total()))
            if st.button("Pagamento",key = ("pagamento")): # Botão ainda sem funcionalidade
                st.write("Botão fora do ar")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
