import streamlit as st
from random import randint
from models.product import Product
catalogo = [Product("The Witcher 3: Wild Hunt","Geraldao ataca novamente!",79.99,"./assets/geralt.png"),
Product("Read Dead Redemption 2","Melhor do que nunca!",99.90,"./assets/ReadDead.jpeg"),
Product("Elden Ring","Anel do Elden!",250.00,"./assets/elden_ring.png"),
Product("Grand Theft Auto 5","Roubei seu PC",99.99,"./assets/gta.png"),
Product("Rainbow Six Siege","Aquele da série do Tom Clancy's",39.99,"./assets/R6.png"),
Product("Stray","Sim, um gato protagonista",59.99,"./assets/Stray.png"),
Product("God Of War: Ragnarok","ELE VOLTOU!",375.00,"./assets/God_Rag.png"),
Product("OverWatch 2","Não, não é de graça!",250.00,"./assets/overwatch.png"),
Product("Outlast Trials","Todos querem esta experiência!",300.00,"./assets/Out_trials.jpg")]

st.set_page_config(page_title="GeraltSteam",layout="centered",initial_sidebar_state="collapsed",menu_items=None)

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
                st.write("Redirecionando...")
            # Botão sem função por enquanto, aguarde novas atualizações...    
        st.error("ERRROUUU 🤣")
        return False
    
    else:
        # Password correct.
        return True

if check_password():
    home,carrinho = st.tabs(["Home","Carrinho"])
    
    with home:
        st.subheader("Temos alguns destaques, confira! 😎")
        col1,col2,col3 = st.columns(3,gap = "small")
        with col1:
            st.image("./assets/geralt.png",caption = "R$ 79,99")
            if st.button(label="Quero você no meu carrinho!",key=randint(0,10000)):
                st.write("Quase lá...")
        
        with col2:
            st.image("./assets/ReadDead.jpeg",caption= "R$ 99,90")
            if st.button(label="Quero você no meu carrinho!",key=randint(0,10000)):
                st.write("Quase lá...")
        with col3:
            st.image("./assets/elden_ring.png", caption = "R$ 250,00")
            if st.button(label="Quero você no meu carrinho!",key=randint(0,10000)):
                st.write("Quase lá...")
                
        col4,col5,col6 = st.columns(3,gap = "small")
        with col4:
            st.image("./assets/gta.png", caption= " R$ 99,99")
            if st.button(label="Quero você no meu carrinho!",key=randint(0,10000)):
                st.write("Quase lá...")
                
        with col5:
            st.image("./assets/R6.png", caption= "R$ 39,90")
            if st.button(label="Quero você no meu carrinho!",key=randint(0,10000)):
                st.write("Quase lá...")
                
        with col6:
            st.image("./assets/Stray.png", caption = "R$ 59,90")
            if st.button(label="Quero você no meu carrinho!",key=randint(0,10000)):
                st.write("Quase lá...")
                
        col7,col8,col9 = st.columns(3,gap = "small")
        with col7:
            st.image("./assets/God_Rag.png",caption= "R$ 375,00")
            if st.button(label="Quero você no meu carrinho!",key=randint(0,10000)):
                st.write("Quase lá...")
                
        with col8:
            st.image("./assets/overwatch.png", caption= "R$ 250,00")
            if st.button(label="Quero você no meu carrinho!",key=randint(0,10000)):
                st.write("Quase lá...")
                
        with col9:
            st.image("./assets/Out_trials.jpg", caption= "R$ 300,00")
            if st.button(label="Quero você no meu carrinho!",key=randint(0,10000)):
                st.write("Quase lá...")
                
    with carrinho:
        col1,col2 = st.columns([3,1],gap = "small")
        with col1:
            st.write("Itens")
        
        with col2:
            st.write("Resumo da Compra:")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
