# Matheus Marins Bernardello RA: 20.00286-6
import streamlit as st
from random import randint
from models.product import Product
from models.carrinho import Carrinho


catalogo = [
Product("The Witcher 3: Wild Hunt","Geraldao ataca novamente!",79.99,"./assets/geralt.png"),
Product("Read Dead Redemption 2","Melhor do que nunca!",99.90,"./assets/ReadDead.jpeg"),
Product("Elden Ring","Anel do Elden!",250.00,"./assets/elden_ring.png"),
Product("Grand Theft Auto 5","Roubei seu PC",99.99,"./assets/gta.png"),
Product("Rainbow Six Siege","Aquele da série do Tom Clancy's",39.99,"./assets/R6.png"),
Product("Stray","Sim, um gato protagonista",59.99,"./assets/Stray.png"),
Product("God Of War: Ragnarok","ELE VOLTOU!",375.00,"./assets/God_Rag.png"),
Product("OverWatch 2","Não, não é de graça!",250.00,"./assets/overwatch.png"),
Product("Outlast Trials","Todos querem esta experiência!",300.00,"./assets/Out_trials.jpg")]

st.set_page_config(page_title="Geraldão_Steam",layout="centered",initial_sidebar_state="collapsed",menu_items=None)

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
    car = Carrinho()
    home,carrinho = st.tabs(["Home","Carrinho"])
    
    with home:
        st.subheader("Temos alguns destaques, confira! 😎")
        st.subheader("Destaques")
        c1,c2,c3 = st.columns(3,gap="small")
        c4,c5,c6 = st.columns(3,gap="small")
        c7,c8,c9 = st.columns(3,gap="small")
        colunas = [c1,c2,c3,c4,c5,c6,c7,c8,c9]
        var = 0
        prod_key_1 = "Produto_"
        for i in colunas:
            with i:
                prod_key_2 = str(var)
                prod_key = prod_key_1+prod_key_2
                st.image(catalogo[var].get_Imagem(),catalogo[var].get_Valor())
                if st.button("Adicionar ao carrinho",key=prod_key):
                    st.write("Produto adicionado ao carrinho!")
                    car.adicionar(catalogo[var])
                var += 1  
                    
                
    with carrinho:
        col1,col2 = st.columns([2,1],gap = "small")
        with col1:
            st.write("Itens:")
            st.write(str(car.exibir_Itens()))
        with col2:
            st.write("Resumo da Compra:")
            st.write(str(car.get_Quantidade_Itens()))
            st.write(str(car.get_Valor_Total()))

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
