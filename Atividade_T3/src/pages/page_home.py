import streamlit as st
from controllers.product_controller import Product_Controller
from controllers.cart_controller import Carrinho
from controllers.loja_controller import Store_Ctrl
from controllers.cart import Cart_Ctrl
from controllers.profile_controller import Profile_Ctrl
#from controllers.admin_controller import Admin_Ctrl

class Home:
    def __init__(self,produtos_db):
        if "carrinho" not in st.session_state:
            st.session_state["carrinho"] = Carrinho()
        if "produtos" not in st.session_state:
            st.session_state["produtos"] = Product_Controller()
        for produto in produtos_db:
            st.session_state["produtos"].adicionar_a_lista(produto)
        
        store,cart,profile,administration = st.tabs(["Loja","Carrinho","Perfil","Novos Produtos"])    
        with store:
            Store_Ctrl()
        with cart:
            Cart_Ctrl()
        with profile:
            Profile_Ctrl()
        with administration:
            #Admin_Ctrl() Falta finalizar esta função 
            pass
        hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
        st.markdown(hide_menu_style, unsafe_allow_html=True)